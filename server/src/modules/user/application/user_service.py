from typing import Optional

from modules.user.application.dtos import (
    CurrentUser,
    UserDTO,
    UserFullDetailsDTO,
    UserPatchDTO,
    UserPatchResponseDTO,
)
from modules.user.domain.entity import User
from modules.user.domain.exceptions import NoPatchDataFoundException, UserNotFoundException
from modules.user.domain.repository_interface import IUserRepository
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    async def create_user_through_clerk(self, user: UserDTO) -> None:
        existing_user = await self.user_repo.get_by_clerk_id(user.clerk_id)
        if existing_user:
            logger.info(f"User already exists for clerk_id: {user.clerk_id}")
            return

        user_obj = User(
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email,
        )
        await self.user_repo.create(user_obj)
        logger.info(f"New user created for clerk_id: {user.clerk_id}")

    async def get_user_by_clerk_id(self, clerk_id: str) -> Optional[CurrentUser]:
        user = await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            raise UserNotFoundException()
        return CurrentUser(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email,
        )

    async def get_user_full_details_by_clerk_id(
        self, clerk_id: str
    ) -> UserFullDetailsDTO:
        user = await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            logger.error(f"User not found for clerk_id: {clerk_id}")
            user = User(clerk_id=clerk_id, name=None, email=None)
            user = await self.user_repo.create(user)
            logger.info(f"New user created for clerk_id: {clerk_id}")

        return UserFullDetailsDTO(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email,
            updated_at=user.updated_at,
            created_at=user.created_at,
        )

    async def patch_user(self, clerk_id: str, patch: UserPatchDTO) -> UserPatchResponseDTO:
        user = await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            raise UserNotFoundException()

        patch_data = patch.model_dump(exclude_none=True)
        if not patch_data:
            raise NoPatchDataFoundException()

        await self.user_repo.update(user, patch_data)
        return UserPatchResponseDTO(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email,
            updated_at=user.updated_at,
            created_at=user.created_at,
        )
