from repositories.user_repository import UserRepository
from models.users import User
from schemas.user_schema import UserDTO
from core.logger import get_scaly_logger
from typing import Optional
logger = get_scaly_logger(name=__name__)

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user: UserDTO) -> Optional[User]:
        user_obj = User(
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email
        )
        return await self.user_repo.create(user_obj)
