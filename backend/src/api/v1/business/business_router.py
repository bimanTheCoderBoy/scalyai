from fastapi import APIRouter
from schemas.business_schema import CreateBusinessDTO, ResponseBusinessDTO,BusinessPatchDTO, BusinessMemberPatchDTO
from core.logger import get_scaly_logger
from api.deps.uow.infrastructure_uow import InfrastructureUnitOfWork
from api.deps import get_uow
from core.exceptions.exceptions import BusinessCreationFailedException, YouAreNotAllowedToAccessThisBusiness, NoPatchDataFoundException, BusinessUpdateDetailsPatchFailedException, BusinessDeletionFailedException, BusinessMemberUpdateFailedException, UserNotFoundException     
from core.exceptions.exceptions import BusinessMemberDeletionFailedException
from fastapi import Depends, HTTPException
from fastapi import Request
from typing import List
from schemas.business_schema import ResponseBusinessMemberDTO

logger = get_scaly_logger(name=__name__)

router = APIRouter(prefix="/api/v1/business", tags=["business"])


@router.post("/", response_model=ResponseBusinessDTO)
async def create_business(request: Request, business: CreateBusinessDTO, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    clerk_id = request.state.user["sub"]

    async with uow:
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        response_business_dto = await uow.business_service.create_business(business, user_id=user.id)
        try:
            await uow.commit()
        except Exception as e:
            await uow.rollback()
            logger.error(f"Error creating business: {e}")
            raise BusinessCreationFailedException()
        return response_business_dto


@router.get("/{business_id}", response_model=ResponseBusinessDTO)
async def get_business_by_id(business_id: int, request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        is_member = await uow.business_member_service.is_user_a_member_of_business(business_id, user_id=user.id)
        if not is_member:
            raise YouAreNotAllowedToAccessThisBusiness()
        business = await uow.business_service.get_business_by_id(business_id)
        return business


@router.patch("/{business_id}", response_model=ResponseBusinessDTO)
async def patch_business(business_id: int, request: Request, patch: BusinessPatchDTO, uow: InfrastructureUnitOfWork = Depends(get_uow)):

    async with uow:
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        have_access = await uow.business_member_service.have_user_access_to_update_or_delete_business(business_id, user_id=user.id)
        if not have_access:
            raise YouAreNotAllowedToAccessThisBusiness()
        patch_data = patch.model_dump(exclude_none=True)
        if not patch_data:
            raise NoPatchDataFoundException()
        updated_business = await uow.business_service.patch_business_details(business_id, patch_data)
        try:
            await uow.commit()
        except Exception as e:
            await uow.rollback()
            logger.error(f"Error patching business: {e}")
            raise BusinessUpdateDetailsPatchFailedException()
        return updated_business
        


@router.delete("/{business_id}", response_model=ResponseBusinessDTO)
async def delete_business(business_id: int, request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        have_access = await uow.business_member_service.have_user_access_to_update_or_delete_business(business_id, user_id=user.id)
        if not have_access:
            raise YouAreNotAllowedToAccessThisBusiness()
        deleted_business = await uow.business_service.delete_business(business_id)
        try:
            await uow.commit()
        except Exception as e:
            await uow.rollback()
            logger.error(f"Error deleting business: {e}")
            raise BusinessDeletionFailedException()
        return deleted_business
        


@router.get("/{business_id}/members", response_model=List[ResponseBusinessMemberDTO])
async def get_members_of_business(business_id: int, request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        is_member = await uow.business_member_service.is_user_a_member_of_business(business_id, user_id=user.id)
        if not is_member:
            raise YouAreNotAllowedToAccessThisBusiness()
        members = await uow.business_member_service.get_members_of_business(business_id)
        return members



@router.patch("/{business_id}/members/{member_id}", response_model=ResponseBusinessMemberDTO)
async def patch_business_member(business_id: int, member_id: int, request: Request, patch: BusinessMemberPatchDTO, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        #checking auth of caller
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        have_access = await uow.business_member_service.have_user_access_to_update_or_delete_business(business_id, user_id=user.id)
        if not have_access:
            raise YouAreNotAllowedToAccessThisBusiness("You are not allowed to update the role or permissions of this member")
        #end

        patch_data = patch.model_dump(exclude_none=True)
        if not patch_data:
            raise NoPatchDataFoundException()
        updated_member = await uow.business_member_service.patch_business_member(business_id, member_id, patch_data)    
        try:
            await uow.commit()
        except Exception as e:
            await uow.rollback()
            logger.error(f"Error patching business member: {e}")
            raise BusinessMemberUpdateFailedException()
        return updated_member

@router.delete("/{business_id}/members/{member_id}", response_model=ResponseBusinessMemberDTO)
async def delete_business_member(business_id: int, member_id: int, request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        #checking auth of caller
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        if user is None:
            raise UserNotFoundException()
        have_access = await uow.business_member_service.have_user_access_to_update_or_delete_business(business_id, user_id=user.id)
        if not have_access:
            raise YouAreNotAllowedToAccessThisBusiness("You are not allowed to delete this member")
        #end
        deleted_member = await uow.business_member_service.delete_business_member(business_id, member_id)
        try:
            await uow.commit()
        except Exception as e:
            await uow.rollback()
            logger.error(f"Error deleting business member: {e}")
            raise BusinessMemberDeletionFailedException()
        return deleted_member