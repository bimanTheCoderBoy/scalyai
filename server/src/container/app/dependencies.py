from config.redis import get_redis
from container.app.infrastructure_uow import InfrastructureUnitOfWork
from container.app.webhook_uow import WebhookUnitOfWork


def get_webhook_uow() -> WebhookUnitOfWork:
    return WebhookUnitOfWork(redis=get_redis())


def get_uow() -> InfrastructureUnitOfWork:
    return InfrastructureUnitOfWork()
