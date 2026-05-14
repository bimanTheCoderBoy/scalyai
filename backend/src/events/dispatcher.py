from schemas.webhook_schema import WebhookEventDTO
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)

class EventDispatcher:


    async def dispatch(self, event: WebhookEventDTO):
        logger.info(f"Dispatching event: {event.type}")
        if event.type.startswith("user."):

            pass # If needed, we can add more handlers here for other events