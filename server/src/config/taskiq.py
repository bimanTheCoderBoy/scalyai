from taskiq.middlewares import SimpleRetryMiddleware
from taskiq.abc.middleware import TaskiqMiddleware
from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend, RedisStreamBroker
from config.settings import taskiq_config
from shared.logger import get_scaly_logger
from config.database import db, init_db
import shared.registry  # noqa: F401  — register all ORM models before task discovery

logger = get_scaly_logger(name=__name__)



class CustomStartupHook(TaskiqMiddleware):
    async def startup(self) -> None:
        logger.info("TaskIQ broker is initializing! Running onstart hook...")
        await init_db() 
        import modules.webhook.infrastructure.worker.clerk_event_task as clerk_event_task # noqa: F401
        
        logger.info("TaskIQ broker initialized successfully...")

    async def shutdown(self) -> None:
        logger.info("TaskIQ broker shutting down...")
        await db.close()
        logger.info("TaskIQ broker shut down successfully...")

result_backend = RedisAsyncResultBackend(
    redis_url=taskiq_config.TASKIQ_RESULT_BACKEND,
    keep_results=True,
    result_ex_time=taskiq_config.TASKIQ_BACKEND_TTL,
)

broker = (
    RedisStreamBroker(
        taskiq_config.TASKIQ_BROKER_URL,
        socket_timeout=None,
        socket_connect_timeout=None,
        consumer_group_name="scalyai_workers",
        additional_streams={
            "clerk_events": ">",
        },
        
    )
    .with_result_backend(result_backend)
    .with_middlewares(SimpleRetryMiddleware(default_retry_count=5), CustomStartupHook())
    
)
