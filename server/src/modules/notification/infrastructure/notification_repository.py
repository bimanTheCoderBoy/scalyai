from typing import List

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from modules.notification.domain.entity import Notification
from modules.notification.domain.exceptions import NotificationCreationFailedException
from modules.notification.domain.repository_interface import INotificationRepository
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class NotificationRepository(INotificationRepository):
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

    async def get_notifications_by_user_id(
        self, user_id: int
    ) -> List[Notification]:
        stmt = select(Notification).where(Notification.user_id == user_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()
