from core.logger import get_scaly_logger
from schemas.webhook_schema import WebhookEventDTO
from repositories.webhook_repository import WebhookRepository
from repositories.cache.webhook_cache import WebhookCacheRepository
from models.webhook_events import WebhookEvent, WebhookEventStatus
logger = get_scaly_logger(name=__name__)

class WebhookService:

    def __init__(
        self,
        cache_repo: WebhookCacheRepository,
        event_repo: WebhookRepository,
    ):
        self.cache_repo = cache_repo
        self.event_repo = event_repo

    async def ingest(self, event: WebhookEventDTO):
        # if await self.cache_repo.is_duplicate(event.event_id):
        #     logger.info(f"Event {event.event_id} is a duplicate")
        #     return

        event_obj = WebhookEvent(
            event_id=event.event_id,
            type=event.type,
            event_timestamp=event.event_timestamp,
            event_status=WebhookEventStatus.PENDING,
            data=event.data
        )
        await self.event_repo.create(event_obj)
        await self.cache_repo.mark_processed(event.event_id)

        from worker.tasks.clerk_events_proess_task import process_clerk_event
        process_clerk_event.delay(event.model_dump(mode="json"))

    async def update_event_status(self, event_id: str, status: WebhookEventStatus):
        await self.event_repo.update_event_status(event_id, status)
