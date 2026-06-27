from core.redis import get_redis
from api.deps.uow.webhook_uow import WebhookUnitOfWork
from api.deps.uow.infrastructure_uow import InfrastructureUnitOfWork


def get_webhook_uow() -> WebhookUnitOfWork:
    return WebhookUnitOfWork(redis=get_redis())


def get_uow() -> InfrastructureUnitOfWork:
    return InfrastructureUnitOfWork()
