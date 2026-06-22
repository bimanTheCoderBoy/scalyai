from fastapi import APIRouter, FastAPI
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from core.exceptions import BaseAppException, handle_api_exception, handle_api_generic_exception
from db import init_db
from api.v1.webhooks.clerk import router as webhooks_router
from api.routes.upload import upload_file
from api.middleware.auth import ClerkAuthMiddleware
from core.redis import init_redis, close_redis

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await init_redis()
    logger.info("Starting ScalyAi API Server...")
    
    yield

    logger.info("Shutting down ScalyAi API Server...")
    await close_redis()


def create_app() -> FastAPI:
    app = FastAPI(
        title="ScalyAi API Server",
        description="API for the ScalyAi project",
        version="0.1.0",
        lifespan=lifespan
    )
    app.add_middleware(ClerkAuthMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(webhooks_router)
    app.add_exception_handler(BaseAppException, handle_api_exception)
    app.add_exception_handler(Exception, handle_api_generic_exception)
    return app


app = create_app()
router = APIRouter()

router.add_api_route("/upload", upload_file, methods=["POST"])

app.include_router(router)