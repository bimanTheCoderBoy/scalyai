from abc import ABC, abstractmethod
from typing import List

from modules.notification.domain.entity import Notification


class INotificationRepository(ABC):
    @abstractmethod
    async def create_notification(self, notification: Notification) -> Notification:
        pass

    @abstractmethod
    async def get_notifications_by_user_id(self, user_id: int) -> List[Notification]:
        pass
