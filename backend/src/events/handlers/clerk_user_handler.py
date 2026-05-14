from schemas.webhook_schema import WebhookEventDTO
from services.user_service import UserService
from services.webhook_service import WebhookService
from schemas.user_schema import UserDTO
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)

class ClerkUserHandler:
    def __init__(self, user_service: UserService, webhook_service: WebhookService):
        self.user_service = user_service
        self.webhook_service = webhook_service

    async def handle(self, event: WebhookEventDTO):
        if event.type == "user.created":
            logger.info(f"Handling user created event: {event.data}")
            user_dto = UserDTO(
                clerk_id=event.data.get("id"),
                name=event.data.get("first_name") + " " + event.data.get("last_name"),
                email=event.data.get("email_addresses",[{"email_address": None}])[0].get("email_address")
            )
            new_user = await self.user_service.create_user(user_dto)
            logger.info(f"User created: {new_user}")
