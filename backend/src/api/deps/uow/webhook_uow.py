from redis.asyncio import Redis
from api.deps.uow.base import BaseUnitOfWork
from repositories.webhook_repository import WebhookRepository
from repositories.cache.webhook_cache import WebhookCacheRepository
from services.webhook_service import WebhookService


class WebhookUnitOfWork(BaseUnitOfWork):
    def __init__(self, redis: Redis, **kwargs):
        super().__init__(**kwargs)
        self._redis = redis
        self._webhook_repo: WebhookRepository | None = None
        self._webhook_cache: WebhookCacheRepository | None = None
        self._webhook_service: WebhookService | None = None

    @property
    def webhook_repo(self) -> WebhookRepository:
        if self._webhook_repo is None:
            self._webhook_repo = WebhookRepository(db=self.session)
        return self._webhook_repo

    @property
    def webhook_cache(self) -> WebhookCacheRepository:
        if self._webhook_cache is None:
            self._webhook_cache = WebhookCacheRepository(cache=self._redis)
        return self._webhook_cache

    @property
    def webhook_service(self) -> WebhookService:
        if self._webhook_service is None:
            self._webhook_service = WebhookService(
                cache_repo=self.webhook_cache,
                event_repo=self.webhook_repo,
            )
        return self._webhook_service
