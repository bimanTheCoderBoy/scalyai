from repositories.user_repository import UserRepository
from models.users import User
from schemas.user_schema import UserDTO
from core.logger import get_scaly_logger
from typing import Optional, Tuple
from models.businesses import Business
from core.exceptions.exceptions import UserNotFoundException,NoPatchDataFoundException
from schemas.user_schema import UserFullDetailsDTO, UserPatchDTO, UserPatchResponseDTO
from schemas.business_schema import BusinessUserDTO
from schemas.user_schema import CurrentUser
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


    async def get_user_by_clerk_id(self, clerk_id: str) -> Optional[CurrentUser]:
        user=await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            raise UserNotFoundException()
        return CurrentUser(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email
        )
    
    async def get_user_full_details_by_clerk_id(self, clerk_id: str) -> UserFullDetailsDTO:
        user = await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            logger.error(f"User not found for clerk_id: {clerk_id}")
            raise UserNotFoundException()

        

        return UserFullDetailsDTO(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name,
            email=user.email,
            updated_at=user.updated_at,
            created_at=user.created_at,
        )    

    async def patch_user(self,clerk_id: str, patch: UserPatchDTO) -> User:
        user = await self.user_repo.get_by_clerk_id(clerk_id)
        if not user:
            raise UserNotFoundException()
        
        patch_data=patch.model_dump(exclude_none=True)
        if not patch_data:
                    raise NoPatchDataFoundException()
        
        await self.user_repo.update(user, patch_data)
        #converting to UserPatchResponseDTO
        user_patch_response_dto = UserPatchResponseDTO(
            id=user.id,
            clerk_id=user.clerk_id,
            name=user.name ,
            email=user.email,
            updated_at=user.updated_at,
            created_at=user.created_at
        )
        return user_patch_response_dto 
        
        


           
