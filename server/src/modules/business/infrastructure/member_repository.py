from typing import List, Optional, Tuple

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from modules.business.domain.entities import Business, BusinessUserMapping
from modules.business.domain.exceptions import (
    BusinessMemberAlreadyExistsException,
    BusinessMemberDeletionFailedException,
    SameValueAlreadyExists,
)
from modules.business.domain.repository_interface import IBusinessMemberRepository
from modules.user.domain.entity import User
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class BusinessMemberRepository(IBusinessMemberRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_member_to_business(
        self, business_user_mapping: BusinessUserMapping
    ) -> BusinessUserMapping:
        try:
            self.db.add(business_user_mapping)
            await self.db.flush()
            return business_user_mapping
        except IntegrityError as e:
            logger.error(f"IntegrityError while adding member to business: {e}")
            raise BusinessMemberAlreadyExistsException()

    async def get_member_by_business_id_and_user_id(
        self, business_id: int, user_id: int
    ) -> Optional[BusinessUserMapping]:
        stmt = (
            select(BusinessUserMapping)
            .options(selectinload(BusinessUserMapping.user))
            .where(
                BusinessUserMapping.business_id == business_id,
                BusinessUserMapping.user_id == user_id,
            )
        )
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_members_of_business(
        self, business_id: int
    ) -> List[Tuple[User, BusinessUserMapping]]:
        stmt = (
            select(User, BusinessUserMapping)
            .select_from(BusinessUserMapping)
            .join(User)
            .where(BusinessUserMapping.business_id == business_id)
        )
        result = await self.db.execute(stmt)
        return result.all()

    async def get_businesses_by_member_id(
        self, member_id: int
    ) -> List[Tuple[BusinessUserMapping, Business]]:
        stmt = (
            select(BusinessUserMapping, Business)
            .select_from(BusinessUserMapping)
            .join(Business)
            .where(BusinessUserMapping.user_id == member_id)
        )
        result = await self.db.execute(stmt)
        return result.all()

    async def update(self, business_member: BusinessUserMapping, data: dict) -> None:
        for key, value in data.items():
            setattr(business_member, key, value)
        try:
            await self.db.flush()
            await self.db.refresh(business_member)
        except IntegrityError as e:
            logger.error(f"IntegrityError while updating business member: {e}")
            raise SameValueAlreadyExists()

    async def delete(self, business_member: BusinessUserMapping) -> None:
        await self.db.delete(business_member)
        try:
            await self.db.flush()
        except IntegrityError as e:
            logger.error(f"IntegrityError while deleting business member: {e}")
            raise BusinessMemberDeletionFailedException()
