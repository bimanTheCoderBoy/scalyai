from db.session import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from services.webhook_service import WebhookService
from repositories.cache.webhook_cache import WebhookCacheRepository
from repositories.webhook_repository import WebhookRepository
from core.redis import get_redis
from fastapi import Depends
from redis.asyncio import Redis

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


async def get_webhook_service(db: AsyncSession = Depends(get_db), cache: Redis = Depends(get_redis)) -> WebhookService:
    return WebhookService(
        cache_repo=WebhookCacheRepository(cache=cache),
        event_repo=WebhookRepository(db=db),
    )
