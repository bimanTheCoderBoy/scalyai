from repositories.invitations_repository import InvitationsRepository
from schemas.invitation_schema import BusinessInviteCreateSchema, BusinessInviteResponseSchema
from models.business_invites import BusinessInvite, BusinessInviteStatus
from pydantic import ValidationError
from core.logger import get_scaly_logger
from core.exceptions.exceptions import BusinessInviteCreationFailedException
from interfaces.notification_interface import NotificationSendServiceInterface
from schemas.notification_schema import NotificationCreateSchema
from models.notifications import NotificationType
logger = get_scaly_logger(name=__name__)

class BusinessInviteService:
    def __init__(self, invitations_repository: InvitationsRepository, notification_send_service: NotificationSendServiceInterface):
        self.invitations_repository = invitations_repository
        self.notification_send_service = notification_send_service

    async def send_invitation(self, invitation: BusinessInviteCreateSchema) -> BusinessInviteResponseSchema:
        invitation = BusinessInvite(
            business_id=invitation.business_id,
            from_user_id=invitation.from_user_id,
            to_user_id=invitation.to_user_id,
            role=invitation.role,
            status=BusinessInviteStatus.PENDING
        )
        
        invitation = await self.invitations_repository.create_invitation(invitation)
        
       
        try:
            return BusinessInviteResponseSchema.model_validate(invitation)
        except ValidationError as e:
            logger.error(f"Error sending invitation: {e}")
            raise BusinessInviteCreationFailedException()