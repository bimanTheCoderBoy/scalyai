from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from core.logger import get_scaly_logger
from core.exceptions.exceptions import UserCreationFailedException, UserAlreadyExistsException
from sqlalchemy import select
from typing import Optional
logger = get_scaly_logger(name=__name__)

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, user: User) -> User:
        try:
            self.db.add(user)
            await self.db.flush()
            return user
        except IntegrityError as e:
            logger.error(f"IntegrityError while creating user: {e}")
            raise UserAlreadyExistsException()
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError while creating user: {e}")
            raise UserCreationFailedException()
    
    async def get_by_clerk_id(self, clerk_id: str) -> Optional[User]:
        stmt = select(User).where(User.clerk_id == clerk_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()