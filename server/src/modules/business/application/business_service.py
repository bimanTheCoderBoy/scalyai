from typing import Optional

from modules.business.application.dtos import CreateBusinessDTO, ResponseBusinessDTO
from modules.business.domain.entities import (
    Business,
    BusinessUserMapping,
    BusinessUserRole,
)
from modules.business.domain.exceptions import BusinessNotFoundException
from modules.business.domain.repository_interface import (
    IBusinessMemberRepository,
    IBusinessRepository,
)
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class BusinessService:
    def __init__(
        self,
        business_repo: IBusinessRepository,
        business_member_repo: IBusinessMemberRepository,
    ):
        self.business_repo = business_repo
        self.business_member_repo = business_member_repo

    async def create_business(
        self, business: CreateBusinessDTO, user_id: int
    ) -> Optional[ResponseBusinessDTO]:
        business_obj = Business(
            name=business.name,
            description=business.description,
            industry=business.industry,
        )
        business = await self.business_repo.create(business_obj)
        business_user_mapping = BusinessUserMapping(
            business_id=business.id,
            user_id=user_id,
            role=BusinessUserRole.OWNER,
            permissions={},
        )
        await self.business_member_repo.add_member_to_business(business_user_mapping)
        response_business_dto = ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at,
        )
        logger.info(f"Business created successfully for id: {business.id}")
        return response_business_dto

    async def get_business_by_id(self, id: int) -> Optional[ResponseBusinessDTO]:
        business = await self.business_repo.get_by_id(id)
        if not business:
            logger.error(f"Business not found for id: {id}")
            raise BusinessNotFoundException()
        return ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at,
        )

    async def patch_business_details(
        self, business_id: int, patch_data: dict
    ) -> Optional[ResponseBusinessDTO]:
        business = await self.business_repo.get_by_id(business_id)
        if not business:
            logger.error(f"Business not found for id: {business_id}")
            raise BusinessNotFoundException()
        await self.business_repo.update(business, patch_data)
        return ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at,
        )

    async def delete_business(self, business_id: int) -> Optional[ResponseBusinessDTO]:
        business = await self.business_repo.get_by_id(business_id)
        if not business:
            logger.error(f"Business not found for id: {business_id}")
            raise BusinessNotFoundException()
        await self.business_repo.delete(business)
        return ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at,
        )
