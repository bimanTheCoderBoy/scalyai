from abc import ABC, abstractmethod

from modules.notification.application.dtos import (
    NotificationCreateSchema,
    NotificationResponseSchema,
)


class NotificationSendServiceInterface(ABC):
    @abstractmethod
    async def push(
        self, notification: NotificationCreateSchema
    ) -> NotificationResponseSchema:
        pass


class PushNotificationServiceInterface(ABC):
    @abstractmethod
    async def push(
        self, notification: NotificationCreateSchema
    ) -> NotificationResponseSchema:
        pass
