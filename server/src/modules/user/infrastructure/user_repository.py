from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from modules.user.domain.entity import User
from modules.user.domain.exceptions import UserAlreadyExistsException
from modules.user.domain.repository_interface import IUserRepository
from modules.business.domain.exceptions import SameValueAlreadyExists
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class UserRepository(IUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user: User) -> User:
        try:
            self.db.add(user)
            await self.db.flush()
            await self.db.refresh(user)
            return user
        except IntegrityError as e:
            logger.error(f"IntegrityError while creating user: {e}")
            raise UserAlreadyExistsException()

    async def get_by_clerk_id(self, clerk_id: str) -> Optional[User]:
        stmt = select(User).where(User.clerk_id == clerk_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, user: User, data: dict) -> User:
        for key, value in data.items():
            setattr(user, key, value)
        try:
            await self.db.flush()
        except IntegrityError as e:
            logger.error(f"IntegrityError while updating user: {e}")
            raise SameValueAlreadyExists()
        await self.db.refresh(user)
        return user
