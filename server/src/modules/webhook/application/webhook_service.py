from modules.webhook.application.dtos import WebhookEventDTO
from modules.webhook.domain.entity import WebhookEvent, WebhookEventStatus
from modules.webhook.domain.repository_interface import (
    IWebhookCacheRepository,
    IWebhookRepository,
)
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class WebhookIngestionService:
    """Used by FastAPI to receive, deduplicate, persist, and enqueue webhook events."""

    def __init__(
        self,
        cache_repo: IWebhookCacheRepository,
        event_repo: IWebhookRepository,
    ):
        self.cache_repo = cache_repo
        self.event_repo = event_repo

    async def ingest(self, event: WebhookEventDTO):
        if await self.cache_repo.is_duplicate(event.event_id):
            logger.info(f"Event {event.event_id} is a duplicate, skipping ingestion")
            return
        logger.info(f"Ingesting event: {event.event_id} {event.type}")
        event_obj = WebhookEvent(
            event_id=event.event_id,
            type=event.type,
            event_timestamp=event.event_timestamp,
            event_status=WebhookEventStatus.PENDING,
            data=event.data,
        )
        await self.event_repo.create(event_obj)

        await self.cache_repo.mark_processed(event.event_id)
        logger.info(f"Event {event.event_id} marked as processed")

        from modules.webhook.infrastructure.worker.clerk_event_task import (
            process_clerk_event,
        )

        await process_clerk_event.kiq(event.model_dump(mode="json"))
        logger.info(f"Event {event.event_id} enqueued for processing")

class WebhookEventService:
    """Used by TaskIQ worker to update webhook event status."""

    def __init__(self, event_repo: IWebhookRepository):
        self.event_repo = event_repo

    async def update_event_status(
        self, event_id: str, status: WebhookEventStatus
    ):
        await self.event_repo.update_event_status(event_id, status)
