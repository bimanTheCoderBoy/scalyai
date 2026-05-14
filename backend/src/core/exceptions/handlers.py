from fastapi.responses import JSONResponse
from .exceptions import BaseAppException
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)
from fastapi import Request

async def handle_api_exception(request: Request, exc: BaseAppException):
    logger.error(f"Exception API: {exc.message} - {exc.status_code}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
   

async def handle_api_generic_exception(request: Request, exc: Exception):
    logger.error(f"Exception Generic: {exc} - {type(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"}
    )
    