from abc import ABC, abstractmethod
from typing import Optional

from modules.user.domain.entity import User


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_clerk_id(self, clerk_id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def update(self, user: User, data: dict) -> User:
        pass
