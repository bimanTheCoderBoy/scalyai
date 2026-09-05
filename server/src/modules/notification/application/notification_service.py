from typing import List

from pydantic import ValidationError

from modules.notification.application.dtos import (
    NotificationCreateSchema,
    NotificationResponseSchema,
)
from modules.notification.domain.entity import Notification
from modules.notification.domain.exceptions import (
    NotificationCreationFailedException,
    NotificationGetFailedException,
)
from modules.notification.domain.repository_interface import INotificationRepository
from modules.notification.domain.service_interface import NotificationSendServiceInterface
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class NotificationService(NotificationSendServiceInterface):
    def __init__(self, notification_repo: INotificationRepository):
        self.notification_repo = notification_repo

    async def push(
        self, notification: NotificationCreateSchema
    ) -> NotificationResponseSchema:
        notification_obj = Notification(
            user_id=notification.user_id,
            title=notification.title,
            message=notification.message,
            type=notification.type,
            extra_data=notification.extra_data or {},
        )
        notification_obj = await self.notification_repo.create_notification(
            notification_obj
        )
        try:
            return NotificationResponseSchema.model_validate(notification_obj)
        except ValidationError as e:
            logger.error(f"Error creating notification: {e}")
            raise NotificationCreationFailedException()

    async def get_notifications(
        self, user_id: int
    ) -> List[NotificationResponseSchema]:
        notifications = await self.notification_repo.get_notifications_by_user_id(
            user_id
        )
        try:
            return [
                NotificationResponseSchema.model_validate(n) for n in notifications
            ]
        except ValidationError as e:
            logger.error(f"Error getting notifications: {e}")
            raise NotificationGetFailedException()
