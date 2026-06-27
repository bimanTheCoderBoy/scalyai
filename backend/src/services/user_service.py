from repositories.user_repository import UserRepository
from models.users import User
from schemas.user_schema import UserDTO
from core.logger import get_scaly_logger
from typing import Optional, Tuple
from models.businesses import Business
from core.exceptions.exceptions import UserNotFoundException
from schemas.user_schema import UserAndBusinessDTO
from schemas.business_schema import BusinessUserDTO
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


    async def get_user_by_clerk_id(self, clerk_id: str) -> Optional[User]:
        user=await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            raise UserNotFoundException()
        
        return user
    
    async def get_user_and_business_by_clerk_id(self, clerk_id: str) -> UserAndBusinessDTO:
        rows = await self.user_repo.get_user_and_business_by_clerk_id(clerk_id)
        if not rows:
            logger.error(f"User not found for clerk_id: {clerk_id}")
            raise UserNotFoundException()

        user = rows[0]["User"]

        return UserAndBusinessDTO(
            name=user.name,
            email=user.email,
            business=[
                BusinessUserDTO(
                    name=row["Business"].name,
                    description=row["Business"].description,
                    industry=row["Business"].industry,
                    permissions=row["BusinessUserMapping"].permissions,
                    role=row["BusinessUserMapping"].role,
                )
                for row in rows if row["Business"] and row["BusinessUserMapping"] 
            ] 
        )    

           
