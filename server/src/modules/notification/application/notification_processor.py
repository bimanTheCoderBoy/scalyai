from modules.notification.application.dtos import (
    NotificationCreateSchema,
    NotificationMessageTemplate,
    NotificationResponseSchema,
)
from modules.notification.domain.entity import NotificationType
from modules.notification.domain.service_interface import PushNotificationServiceInterface
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class NotificationMessageTemplateFactory:
    _TEMPLATE_REGISTRY = {
        NotificationType.INVITATION: NotificationMessageTemplate(
            title="You have been invited to a new business",
            message="You have been invited to a new business by {from_user_name} to join {business_name} as {role}.",
        ),
    }

    @classmethod
    def get_template(
        cls, notification_type: NotificationType
    ) -> NotificationMessageTemplate:
        template = cls._TEMPLATE_REGISTRY.get(notification_type)
        if not template:
            raise ValueError(
                f"No template found for notification type: {notification_type}"
            )
        return template


class NotificationProcessorService:
    def __init__(
        self, push_notification_service: PushNotificationServiceInterface
    ):
        self.push_notification_service = push_notification_service

    def process(
        self, notification: NotificationCreateSchema
    ) -> NotificationResponseSchema:
        template = NotificationMessageTemplateFactory.get_template(
            notification_type=notification.type
        )
        # TODO: format template with actual data and push via push_notification_service
        ...
