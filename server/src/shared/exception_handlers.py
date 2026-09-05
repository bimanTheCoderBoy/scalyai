from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from shared.base_exception import BaseAppException
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


async def handle_api_exception(request: Request, exc: BaseAppException):
    logger.error(f"Exception API: {exc.message} - {exc.status_code}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


async def handle_api_generic_exception(request: Request, exc: Exception):
    logger.error(f"Exception Generic: {exc} - {type(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"},
    )


async def handle_api_database_exception(request: Request, exc: SQLAlchemyError):
    logger.error(f"Database Exception: {exc} - {type(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected database error occurred"},
    )
