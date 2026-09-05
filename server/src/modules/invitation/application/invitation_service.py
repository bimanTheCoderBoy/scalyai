from pydantic import ValidationError

from modules.invitation.application.dtos import (
    BusinessInviteCreateSchema,
    BusinessInviteResponseSchema,
)
from modules.invitation.domain.entity import BusinessInvite, BusinessInviteStatus
from modules.invitation.domain.exceptions import BusinessInviteCreationFailedException
from modules.invitation.domain.repository_interface import IInvitationRepository
from modules.notification.domain.service_interface import NotificationSendServiceInterface
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class BusinessInviteService:
    def __init__(
        self,
        invitations_repository: IInvitationRepository,
        notification_send_service: NotificationSendServiceInterface,
    ):
        self.invitations_repository = invitations_repository
        self.notification_send_service = notification_send_service

    async def send_invitation(
        self, invitation: BusinessInviteCreateSchema
    ) -> BusinessInviteResponseSchema:
        invitation_obj = BusinessInvite(
            business_id=invitation.business_id,
            from_user_id=invitation.from_user_id,
            to_user_id=invitation.to_user_id,
            role=invitation.role,
            status=BusinessInviteStatus.PENDING,
        )

        invitation_obj = await self.invitations_repository.create_invitation(
            invitation_obj
        )

        try:
            return BusinessInviteResponseSchema.model_validate(invitation_obj)
        except ValidationError as e:
            logger.error(f"Error sending invitation: {e}")
            raise BusinessInviteCreationFailedException()
