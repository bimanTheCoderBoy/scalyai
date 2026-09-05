from redis.asyncio import Redis

from modules.webhook.application.webhook_service import WebhookIngestionService
from modules.webhook.infrastructure.webhook_cache_repository import (
    WebhookCacheRepository,
)
from modules.webhook.infrastructure.webhook_repository import WebhookRepository
from shared.uow import BaseUnitOfWork


class WebhookUnitOfWork(BaseUnitOfWork):
    def __init__(self, redis: Redis):
        super().__init__()
        self._redis = redis
        self._webhook_repo: WebhookRepository | None = None
        self._webhook_cache: WebhookCacheRepository | None = None
        self._webhook_service: WebhookIngestionService | None = None

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
    def webhook_service(self) -> WebhookIngestionService:
        if self._webhook_service is None:
            self._webhook_service = WebhookIngestionService(
                cache_repo=self.webhook_cache,
                event_repo=self.webhook_repo,
            )
        return self._webhook_service
