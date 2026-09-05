from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from modules.business.domain.entities import Business, BusinessUserMapping
from modules.user.domain.entity import User


class IBusinessRepository(ABC):
    @abstractmethod
    async def create(self, business: Business) -> Business:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[Business]:
        pass

    @abstractmethod
    async def update(self, business: Business, data: dict) -> None:
        pass

    @abstractmethod
    async def delete(self, business: Business) -> None:
        pass


class IBusinessMemberRepository(ABC):
    @abstractmethod
    async def add_member_to_business(
        self, business_user_mapping: BusinessUserMapping
    ) -> BusinessUserMapping:
        pass

    @abstractmethod
    async def get_member_by_business_id_and_user_id(
        self, business_id: int, user_id: int
    ) -> Optional[BusinessUserMapping]:
        pass

    @abstractmethod
    async def get_members_of_business(
        self, business_id: int
    ) -> List[Tuple[User, BusinessUserMapping]]:
        pass

    @abstractmethod
    async def get_businesses_by_member_id(
        self, member_id: int
    ) -> List[Tuple[BusinessUserMapping, Business]]:
        pass

    @abstractmethod
    async def update(self, business_member: BusinessUserMapping, data: dict) -> None:
        pass

    @abstractmethod
    async def delete(self, business_member: BusinessUserMapping) -> None:
        pass
