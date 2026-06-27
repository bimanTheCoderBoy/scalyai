from sqlalchemy.ext.asyncio import AsyncSession
from models.business_user_mappings import BusinessUserMapping
from typing import Optional
from core.logger import get_scaly_logger
from models.users import User
from models.business_user_mappings import BusinessUserRole
from core.exceptions.exceptions import BusinessMemberAlreadyExistsException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from typing import List, Tuple
from models.businesses import Business
logger = get_scaly_logger(name=__name__)

class BusinessMemberRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def add_member_to_business(self, business_user_mapping: BusinessUserMapping):

        try:
            self.db.add(business_user_mapping)
            await self.db.flush()
            return business_user_mapping
        except IntegrityError as e:
            logger.error(f"IntegrityError while adding member to business: {e}")
            raise BusinessMemberAlreadyExistsException()
    
    async def get_member_by_business_id_and_user_id(self, business_id: int, user_id: int) -> Optional[BusinessUserMapping]:
        stmt = select(BusinessUserMapping).where(BusinessUserMapping.business_id == business_id, BusinessUserMapping.user_id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
        
    async def get_members_of_business(self, business_id: int) -> List[Tuple[User, BusinessUserMapping]]:
        stmt=select(User, BusinessUserMapping).select_from(BusinessUserMapping).join(User).where(BusinessUserMapping.business_id == business_id)
        result = await self.db.execute(stmt)
        return result.all()
    
    async def get_businesses_by_member_id(self, member_id: int) -> List[Tuple[BusinessUserMapping, Business]]:
        stmt=select(BusinessUserMapping, Business).select_from(BusinessUserMapping).join(Business).where(BusinessUserMapping.user_id == member_id)
        result = await self.db.execute(stmt)
        return result.all()
