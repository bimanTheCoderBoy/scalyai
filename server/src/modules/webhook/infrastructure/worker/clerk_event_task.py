from typing import Annotated

from taskiq import TaskiqDepends

from config.taskiq import broker
from container.worker.webhook_worker_uow import WebhookWorkerUnitOfWork
from container.worker.dependencies import get_webhook_worker_uow
from modules.webhook.application.dtos import WebhookEventDTO
from modules.webhook.domain.entity import WebhookEventStatus
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)





@broker.task(
    task_name="tasks.process_clerk_event",
    queue_name="clerk_events",
    retry_on_error=True,
    max_retries=5,
)
async def process_clerk_event(
    event_data: dict,
    uow: Annotated[WebhookWorkerUnitOfWork, TaskiqDepends(get_webhook_worker_uow)],
) -> None:
    event = WebhookEventDTO.model_validate(event_data)
    logger.info(f"Event type: {event.type}, Event data keys: {event.data.keys()}")

    try:
        await uow.event_service.update_event_status(
            event.event_id, WebhookEventStatus.PROCESSING
        )
        success = await uow.clerk_handler.handle(event)

        final_status = (
            WebhookEventStatus.COMPLETED if success else WebhookEventStatus.SKIPPED
        )
        await uow.event_service.update_event_status(event.event_id, final_status)
        await uow.commit()

        logger.info(f"Successfully processed clerk event: {event.event_id}")

    except Exception as exc:
        await uow.rollback()
        logger.error(f"Failed to process clerk event {event.event_id}: {exc}")
        await _mark_failed(event.event_id)
        raise


async def _mark_failed(event_id: str) -> None:
    async with WebhookWorkerUnitOfWork() as uow:
        try:
            await uow.event_service.update_event_status(
                event_id, WebhookEventStatus.FAILED
            )
            await uow.commit()
        except Exception as e:
            logger.error(f"Failed to mark event {event_id} as FAILED: {e}")
