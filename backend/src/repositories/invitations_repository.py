from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.business_invites import BusinessInvite
from core.logger import get_scaly_logger
from core.exceptions.exceptions import BusinessInviteAlreadyExistsException
from typing import Optional, List
from sqlalchemy import select
from models.business_invites import BusinessInviteStatus
from core.exceptions.exceptions import BusinessInviteAcceptanceFailedException, BusinessInviteRejectionFailedException, BusinessInviteCancellationFailedException
logger = get_scaly_logger(name=__name__)

class InvitationsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        try:
            self.db.add(invitation)
            await self.db.flush()
            await self.db.refresh(invitation)
            return invitation
        except IntegrityError as e:
            logger.error(f"IntegrityError while creating invitation: {e}")
            raise BusinessInviteAlreadyExistsException()
        

    async def get_invitations_send_by_user_id_and_business_id(self, user_id: int, business_id: int) -> List[BusinessInvite]:
        stmt = select(BusinessInvite).where(BusinessInvite.from_user_id == user_id, BusinessInvite.business_id == business_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()
    
    async def accept_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        invitation.status = BusinessInviteStatus.ACCEPTED
        try:
            await self.db.flush()
            await self.db.refresh(invitation)
            return invitation
        except IntegrityError as e:
            logger.error(f"IntegrityError while accepting invitation: {e}")
            raise BusinessInviteAcceptanceFailedException()
    
    async def reject_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        invitation.status = BusinessInviteStatus.REJECTED
        try:
            await self.db.flush()
            await self.db.refresh(invitation)
            return invitation
        except IntegrityError as e:
            logger.error(f"IntegrityError while rejecting invitation: {e}")
            raise BusinessInviteRejectionFailedException()
    
    async def cancel_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        invitation.status = BusinessInviteStatus.CANCELLED
        try:
            await self.db.flush()
            await self.db.refresh(invitation)
            return invitation
        except IntegrityError as e:
            logger.error(f"IntegrityError while cancelling invitation: {e}")
            raise BusinessInviteCancellationFailedException()

    