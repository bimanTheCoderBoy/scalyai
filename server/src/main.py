from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError

from config.database import db, init_db
from config.redis import close_redis, init_redis
from modules.business.presentation.router import router as business_router
from modules.invitation.presentation.router import router as invitation_router
from modules.user.presentation.router import router as user_router
from modules.webhook.presentation.router import router as webhook_router
from shared.base_exception import BaseAppException
from shared.exception_handlers import (
    handle_api_database_exception,
    handle_api_exception,
    handle_api_generic_exception,
)
from shared.logger import get_scaly_logger
from shared.middleware.auth import ClerkAuthMiddleware
from config.taskiq import broker
logger = get_scaly_logger(name=__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting ScalyAi Server...")
    await init_db()
    logger.info("Database initialized successfully...")
    await init_redis()
    logger.info("Redis initialized successfully...")
    if not broker.is_worker_process:
        await broker.startup()
    logger.info("Broker initialized successfully...")
    logger.info("ScalyAi Server started successfully...")
    yield
    logger.info("ScalyAi Server shutting down...")
    await close_redis()
    logger.info("Redis closed successfully...")
    await db.close()
    logger.info("Database closed successfully...")
    if broker.is_worker_process:
        await broker.shutdown()
    logger.info("Broker closed successfully...")
    logger.info("ScalyAi Server shut down successfully...")

def create_app() -> FastAPI:
    app = FastAPI(
        title="ScalyAi Server",
        description="DDD-based API Server for ScalyAi",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(ClerkAuthMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_router)
    app.include_router(business_router)
    app.include_router(invitation_router)
    app.include_router(webhook_router)

    app.add_exception_handler(BaseAppException, handle_api_exception)
    app.add_exception_handler(SQLAlchemyError, handle_api_database_exception)
    app.add_exception_handler(Exception, handle_api_generic_exception)

    return app


app = create_app()
