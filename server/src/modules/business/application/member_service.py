from typing import List

from modules.business.application.dtos import BusinessUserDTO, ResponseBusinessMemberDTO
from modules.business.domain.entities import BusinessUserRole
from modules.business.domain.exceptions import (
    BusinessMemberNotFoundException,
    BusinessNotFoundException,
)
from modules.business.domain.repository_interface import (
    IBusinessMemberRepository,
    IBusinessRepository,
)
from modules.user.domain.repository_interface import IUserRepository
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class BusinessMemberService:
    def __init__(
        self,
        business_member_repo: IBusinessMemberRepository,
        business_repo: IBusinessRepository,
        user_repo: IUserRepository,
    ):
        self.business_member_repo = business_member_repo
        self.business_repo = business_repo
        self.user_repo = user_repo

    async def is_user_a_member_of_business(
        self, business_id: int, user_id: int
    ) -> bool:
        mapping = await self.business_member_repo.get_member_by_business_id_and_user_id(
            business_id, user_id
        )
        return mapping is not None

    async def have_user_access_to_update_or_delete_business(
        self, business_id: int, user_id: int
    ) -> bool:
        mapping = await self.business_member_repo.get_member_by_business_id_and_user_id(
            business_id, user_id
        )
        if not mapping:
            return False
        return mapping.role in (BusinessUserRole.OWNER, BusinessUserRole.ADMIN)

    async def get_members_of_business(
        self, business_id: int
    ) -> List[ResponseBusinessMemberDTO]:
        business = await self.business_repo.get_by_id(business_id)
        if not business:
            logger.error(f"Business not found for id: {business_id}")
            raise BusinessNotFoundException()
        members = await self.business_member_repo.get_members_of_business(business_id)
        return [
            ResponseBusinessMemberDTO(
                id=user.id,
                name=user.name,
                email=user.email,
                role=business_user_mapping.role,
                permissions=business_user_mapping.permissions,
            )
            for user, business_user_mapping in members
        ]

    async def get_businesses_by_member_id(
        self, member_id: int
    ) -> List[BusinessUserDTO]:
        businesses = await self.business_member_repo.get_businesses_by_member_id(
            member_id
        )
        return [
            BusinessUserDTO(
                name=business.name,
                description=business.description,
                industry=business.industry,
                permissions=business_user_mapping.permissions,
                role=business_user_mapping.role,
            )
            for business_user_mapping, business in businesses
        ]

    async def patch_business_member(
        self, business_id: int, member_id: int, patch_data: dict
    ) -> ResponseBusinessMemberDTO:
        business_member = (
            await self.business_member_repo.get_member_by_business_id_and_user_id(
                business_id, member_id
            )
        )
        if not business_member:
            logger.error(f"Business member not found for id: {member_id}")
            raise BusinessMemberNotFoundException()
        await self.business_member_repo.update(business_member, patch_data)
        return ResponseBusinessMemberDTO(
            id=member_id,
            name=business_member.user.name,
            email=business_member.user.email,
            role=business_member.role,
            permissions=business_member.permissions,
        )

    async def delete_business_member(
        self, business_id: int, member_id: int
    ) -> ResponseBusinessMemberDTO:
        business_member = (
            await self.business_member_repo.get_member_by_business_id_and_user_id(
                business_id, member_id
            )
        )
        if not business_member:
            logger.error(f"Business member not found for id: {member_id}")
            raise BusinessMemberNotFoundException()
        await self.business_member_repo.delete(business_member)
        return ResponseBusinessMemberDTO(
            id=member_id,
            name=business_member.user.name,
            email=business_member.user.email,
            role=business_member.role,
            permissions=business_member.permissions,
        )
