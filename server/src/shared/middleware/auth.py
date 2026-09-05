import httpx
import jwt
from fastapi import status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from config.settings import clerk_config, security_config
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)

_jwks_cache: dict | None = None


async def _get_jwks() -> dict:
    global _jwks_cache
    if _jwks_cache:
        return _jwks_cache

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{clerk_config.CLERK_PUBLIC_KEY_URL}")
        resp.raise_for_status()
        _jwks_cache = resp.json()
        return _jwks_cache


class ClerkAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not any(
            path in request.url.path for path in security_config.PRIVATE_PATHS
        ):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            logger.error(
                f"Missing or invalid Authorization header for path: {request.url.path}"
            )
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing or invalid Authorization header"},
            )

        token = auth_header.split(" ", 1)[1]
        issuer = clerk_config.CLERK_ISSUER

        try:
            jwks = await _get_jwks()
            header = jwt.get_unverified_header(token)

            rsa_key = None
            for key in jwks["keys"]:
                if key["kid"] == header["kid"]:
                    rsa_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break

            if not rsa_key:
                logger.error(
                    f"Unable to find signing key for path: {request.url.path}"
                )
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "Unable to find signing key"},
                )

            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                issuer=issuer,
            )
            if not payload["sub"]:
                logger.error(
                    f"User ID is missing from the token for path: {request.url.path}"
                )
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "User ID is missing from the token"},
                )
            request.state.user = payload

        except jwt.ExpiredSignatureError:
            logger.error(f"Token has expired: {token}")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Token has expired"},
            )
        except jwt.InvalidTokenError:
            logger.error(f"Invalid token: {token}")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid token"},
            )
        logger.info(f"User authenticated: {payload}")
        return await call_next(request)
