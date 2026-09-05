from abc import ABC, abstractmethod
from schemas.notification_schema import NotificationCreateSchema, NotificationResponseSchema
from typing import List

class PushNotificationServiceInterface(ABC):
  
    @abstractmethod
    async def push(self, notification: NotificationCreateSchema) -> NotificationResponseSchema:
        pass
   