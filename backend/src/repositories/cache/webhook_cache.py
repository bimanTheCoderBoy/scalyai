from redis import Redis,RedisError
from core.logger import get_scaly_logger
from core.exceptions.exceptions import WebhookCacheError
logger = get_scaly_logger(name=__name__)

class WebhookCacheRepository:
    def __init__(self, cache: Redis, ttl: int = 60 * 60 * 24):
        self.cache = cache
        self.ttl = ttl

    def _build_key(
        self,
        event_id: str
    ) -> str:

        return f"webhook:event:{event_id}"

    async def is_duplicate(
        self,
        event_id: str
    ) -> bool:

        key = self._build_key(event_id)
        try:
            exists = await self.cache.exists(key)
            return bool(exists)
        except RedisError as e:
            logger.error(f"RedisError while checking if event is duplicate: {e}")
            raise WebhookCacheError()
    

    async def mark_processed(
        self,
        event_id: str
    ) -> None:
        key = self._build_key(event_id)
        try:
            await self.cache.set(key, "processed", ex=self.ttl)
            return event_id
        except RedisError as e:
            logger.error(f"RedisError while marking event as processed: {e}")
            raise WebhookCacheError()
        
    
    async def remove(
        self,
        event_id: str
    ) -> None:
        key = self._build_key(event_id)
        try:
            await self.cache.delete(key)
            return True
        except RedisError as e:
            logger.error(f"RedisError while removing event: {e}")
            raise WebhookCacheError()
        
