from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.businesses import Business
from models.business_user_mappings import BusinessUserMapping
from typing import Optional, List, Tuple    
from sqlalchemy import select
from core.logger import get_scaly_logger
from core.exceptions.exceptions import BusinessAlreadyExistsException, SameValueAlreadyExists, BusinessDeletionFailedException
from models.users import User
logger = get_scaly_logger(name=__name__)


class BusinessRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, business: Business) -> Business:
        try:
            self.db.add(business)
            await self.db.flush()
            return business
        except IntegrityError as e:
            logger.error(f"IntegrityError while creating business: {e}")
            raise BusinessAlreadyExistsException()
       
   
    async def get_by_id(self, id: int) -> Optional[Business]:
        stmt = select(Business).where(Business.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, business: Business, data: dict) -> None:
        for key, value in data.items():
            setattr(business, key, value)
        try:
            await self.db.flush()
            await self.db.refresh(business)
        except IntegrityError as e:
            logger.error(f"IntegrityError while updating business: {e}")
            raise SameValueAlreadyExists()


    async def delete(self, business: Business) -> None:
        await self.db.delete(business)
        try:
            await self.db.flush()
        except IntegrityError as e:
            logger.error(f"IntegrityError while deleting business: {e}")
            raise BusinessDeletionFailedException()
        
    
   