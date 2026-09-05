from abc import ABC, abstractmethod
from typing import List, Optional

from modules.invitation.domain.entity import BusinessInvite


class IInvitationRepository(ABC):
    @abstractmethod
    async def create_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        pass

    @abstractmethod
    async def get_invitations_send_by_user_id_and_business_id(
        self, user_id: int, business_id: int
    ) -> List[BusinessInvite]:
        pass

    @abstractmethod
    async def accept_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        pass

    @abstractmethod
    async def reject_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        pass

    @abstractmethod
    async def cancel_invitation(self, invitation: BusinessInvite) -> BusinessInvite:
        pass
