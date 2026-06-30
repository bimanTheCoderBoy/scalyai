from sqlalchemy.ext.asyncio import AsyncSession
from models.webhook_events import WebhookEvent
from schemas.webhook_schema import WebhookEventDTO
from models.webhook_events import WebhookEventStatus
from sqlalchemy import select,update
from typing import Optional
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from core.logger import get_scaly_logger
from core.exceptions.exceptions import WebhookEventAlreadyExistsException, WebhookEventCreationFailedException, WebhookEventUpdateFailedException
logger = get_scaly_logger(name=__name__)

class WebhookRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, event: WebhookEvent):
        try:
            
            self.db.add(event)
            await self.db.flush()
            return event

        except IntegrityError as e:
            logger.error(f"IntegrityError while creating webhook event: {e}")
            raise WebhookEventAlreadyExistsException()
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError while creating webhook event: {e}")
            raise WebhookEventCreationFailedException()

    async def get_by_event_id(
        self,
        event_id: str
    ) -> Optional[WebhookEvent]:

        stmt = select(WebhookEvent).where(
            WebhookEvent.event_id == event_id
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()


    async def update_event_status(
        self,
        event_id :str,
        status: WebhookEventStatus):
        try:
            stmt = update(WebhookEvent).where(WebhookEvent.event_id == event_id).values(event_status=status)
            await self.db.execute(stmt)
            await self.db.flush()
            return event_id

        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError while updating event status: {e}")
            raise WebhookEventUpdateFailedException()