from fastapi import APIRouter
from schemas.user_schema import UserFullDetailsDTO, UserPatchDTO, UserPatchResponseDTO
from fastapi import Request, Depends
from api.deps.uow.infrastructure_uow import InfrastructureUnitOfWork
from api.deps import get_uow
from core.exceptions.exceptions import UserGetFailedException, UserPatchFailedException, UserNotFoundException
from typing import List
from schemas.business_schema import BusinessUserDTO

router = APIRouter(prefix="/api/v1/me", tags=["users"])


@router.get("/", response_model=UserFullDetailsDTO)
async def get_me(request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    clerk_id = request.state.user["sub"]
    async with uow:
        user_full_details: UserFullDetailsDTO = await uow.user_service.get_user_full_details_by_clerk_id(clerk_id)
        try:
            await uow.commit()
        except Exception:
            await uow.rollback()
            raise UserGetFailedException()
        return user_full_details


@router.patch("/", response_model=UserPatchResponseDTO)
async def update_me(request: Request, patch: UserPatchDTO, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    clerk_id = request.state.user["sub"]

    async with uow:
        user_patch_response_dto = await uow.user_service.patch_user(clerk_id, patch)
        try:
            await uow.commit()
        except Exception:
            await uow.rollback()
            raise UserPatchFailedException()
        return user_patch_response_dto


@router.get("/businesses", response_model=List[BusinessUserDTO])
async def get_businesses(request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    clerk_id = request.state.user["sub"]
    async with uow:
        user = await uow.user_service.get_user_by_clerk_id(clerk_id)
        businesses = await uow.business_member_service.get_businesses_by_member_id(user.id)
        return businesses
