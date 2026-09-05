from sqlalchemy.ext.asyncio import AsyncSession
from core.logger import get_scaly_logger
from core.exceptions.exceptions import NotificationCreationFailedException
from models.notifications import Notification
from sqlalchemy.exc import IntegrityError
from typing import List
from sqlalchemy import select
logger = get_scaly_logger(name=__name__)

class NotificationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_notification(self, notification: Notification) -> Notification:
        try:
            self.db.add(notification)
            await self.db.flush()
            await self.db.refresh(notification)
            return notification
        except IntegrityError as e:
            logger.error(f"IntegrityError while creating notification: {e}")
            raise NotificationCreationFailedException()
            
    async def get_notifications_by_user_id(self, user_id: int) -> List[Notification]:
        stmt = select(Notification).where(Notification.user_id == user_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()