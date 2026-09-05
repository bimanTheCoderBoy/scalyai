from typing import AsyncGenerator
from container.worker.webhook_worker_uow import WebhookWorkerUnitOfWork

async def get_webhook_worker_uow() -> AsyncGenerator[WebhookWorkerUnitOfWork, None]:
    async with WebhookWorkerUnitOfWork() as uow:
        yield uow