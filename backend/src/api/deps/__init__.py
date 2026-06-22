from core.redis import get_redis
from api.deps.uow.webhook_uow import WebhookUnitOfWork


def get_webhook_uow() -> WebhookUnitOfWork:
    return WebhookUnitOfWork(redis=get_redis())
