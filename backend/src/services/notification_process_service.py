from interfaces.notification_interface import PushNotificationServiceInterface
from schemas.notification_schema import NotificationCreateSchema, NotificationResponseSchema, NotificationMessageTemplate
from models.notifications import Notification, NotificationType
from pydantic import ValidationError
from core.logger import get_scaly_logger
from core.exceptions.exceptions import NotificationCreationFailedException, NotificationGetFailedException
from typing import List
logger = get_scaly_logger(name=__name__)

class NotificationMessageTemplateFactory:
    _TEMPLATE_REGISTRY = {
        NotificationType.INVITATION: NotificationMessageTemplate(
            title="You have been invited to a new business",
            message="You have been invited to a new business by {from_user_name} to join {business_name} as {role}.",
        )
    }
    @classmethod
    def get_template(cls, notification_type: NotificationType) -> NotificationMessageTemplate:
        template = cls._TEMPLATE_REGISTRY.get(notification_type)
        if not template:
            raise ValueError(f"No template found for notification type: {notification_type}")
        return template


class NotificationProcessorService:
    def __init__(self, push_notification_service: PushNotificationServiceInterface):
        self.push_notification_service = push_notification_service
    
    def process(self,notification: NotificationCreateSchema)->NotificationResponseSchema:

        #Get Template from resgistry
        template:NotificationMessageTemplate=NotificationMessageTemplateFactory.get_template(notification_type=notification.type)



















    # async def send_notification(self, notification: NotificationCreateSchema) -> NotificationResponseSchema:
    #     notification = Notification(
    #         user_id=notification.user_id,
    #         title=notification.title,
    #         message=notification.message,
    #         type=notification.type,
    #         extra_data=notification.extra_data or {}
    #     )
    #     notification = await self.notification_repository.create_notification(notification)
    #     try:
    #         return NotificationResponseSchema.model_validate(notification)
    #     except ValidationError as e:
    #         logger.error(f"Error creating notification: {e}")
    #         raise NotificationCreationFailedException()

            
    # async def get_notifications(self, user_id: int) -> List[NotificationResponseSchema]:
    #     notifications = await self.notification_repository.get_notifications_by_user_id(user_id)
    #     try:
    #         return [NotificationResponseSchema.model_validate(notification) for notification in notifications]
    #     except ValidationError as e:
    #         logger.error(f"Error getting notifications: {e}")
    #         raise NotificationGetFailedException()