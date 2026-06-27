from repositories.business_repository import BusinessRepository
from models.businesses import Business
from schemas.business_schema import CreateBusinessDTO, ResponseBusinessDTO
from typing import Optional
from core.logger import get_scaly_logger
from core.exceptions.exceptions import BusinessNotFoundException, BusinessMemberAdditionFailedException
from repositories.business_member_repository import BusinessMemberRepository
from models.business_user_mappings import BusinessUserMapping, BusinessUserRole
logger = get_scaly_logger(name=__name__)

class BusinessService:
    def __init__(self, business_repo: BusinessRepository, business_member_repo: BusinessMemberRepository):
        self.business_repo = business_repo
        self.business_member_repo = business_member_repo

    async def create_business(self, business: CreateBusinessDTO, user_id: int) -> Optional[ResponseBusinessDTO]:
        business_obj = Business(
            name=business.name,
            description=business.description,
            industry=business.industry
        )
        business = await self.business_repo.create(business_obj)
        #Create mapping for the business
        business_user_mapping = BusinessUserMapping(
            business_id=business.id,
            user_id=user_id,
            role=BusinessUserRole.OWNER,
            permissions={}
        )
        await self.business_member_repo.add_member_to_business(business_user_mapping)
        response_business_dto = ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at
        )
        logger.info(f"Business created successfully for id: {business.id}")
        return response_business_dto
    
    async def get_business_by_id(self, id: int) -> Optional[ResponseBusinessDTO]:
        business = await self.business_repo.get_by_id(id)
        if not business:
            logger.error(f"Business not found for id: {id}")
            raise BusinessNotFoundException()
        response_business_dto = ResponseBusinessDTO(
            id=business.id,
            name=business.name,
            description=business.description,
            industry=business.industry,
            created_at=business.created_at,
            updated_at=business.updated_at
        )   
        return response_business_dto
    
    