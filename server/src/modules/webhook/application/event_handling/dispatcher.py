from modules.webhook.application.dtos import WebhookEventDTO
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class EventDispatcher:
    async def dispatch(self, event: WebhookEventDTO):
        logger.info(f"Dispatching event: {event.type}")
        if event.type.startswith("user."):
            pass
