from redis.asyncio import Redis
from core.config import redis_config
from core.logger import get_scaly_logger
from core.exceptions.exceptions import RedisClientNotInitializedError
logger = get_scaly_logger(name=__name__)

redis_client: Redis | None = None


async def init_redis():
    global redis_client

    logger.info("Initializing Redis client...")
    redis_client = Redis(
        host=redis_config.REDIS_HOST,
        port=redis_config.REDIS_PORT,
        db=redis_config.REDIS_DB,
        decode_responses=True
    )
    logger.info("Redis client initialized successfully...")


async def close_redis():
    global redis_client

    if redis_client:
        await redis_client.close()
        logger.info("Redis client closed successfully...")


def get_redis() -> Redis:
    global redis_client
    if redis_client is None:
        
        raise RedisClientNotInitializedError()
    return redis_client