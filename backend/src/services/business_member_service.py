from repositories.business_member_repository import BusinessMemberRepository
from typing import List
from schemas.business_schema import ResponseBusinessMemberDTO
from repositories.business_repository import BusinessRepository
from core.logger import get_scaly_logger
from core.exceptions.exceptions import BusinessNotFoundException
from repositories.user_repository import UserRepository
from schemas.business_schema import BusinessUserDTO
logger = get_scaly_logger(name=__name__)

class BusinessMemberService:
    def __init__(self, business_member_repo: BusinessMemberRepository, business_repo: BusinessRepository, user_repo: UserRepository):
        self.business_member_repo = business_member_repo
        self.business_repo = business_repo  
        self.user_repo = user_repo
    

    async def is_user_a_member_of_business(self, business_id: int, user_id: int) -> bool:
        
        business_user_mapping = await self.business_member_repo.get_member_by_business_id_and_user_id(business_id, user_id)
        if not business_user_mapping:
            return False
        return True


    async def get_members_of_business(self, business_id: int) -> List[ResponseBusinessMemberDTO]: 
        # is business id valid?
        business = await self.business_repo.get_by_id(business_id)
        if not business:
            logger.error(f"Business not found for id: {business_id}")       
            raise BusinessNotFoundException()
        #get the members of the business
        members = await self.business_member_repo.get_members_of_business(business_id)
        
        return [ResponseBusinessMemberDTO(
            name=user.name,
            email=user.email,
            role=business_user_mapping.role,
            permissions=business_user_mapping.permissions
        ) for user, business_user_mapping in members]
    
    async def get_businesses_by_member_id(self, member_id: int) -> List[BusinessUserDTO]:


        businesses = await self.business_member_repo.get_businesses_by_member_id(member_id)
        return [BusinessUserDTO(
            name=business.name,
            description=business.description,
            industry=business.industry,
            permissions=business_user_mapping.permissions,
            role=business_user_mapping.role
        ) for business_user_mapping, business in businesses]