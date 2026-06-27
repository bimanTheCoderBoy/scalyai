from fastapi import APIRouter
from schemas.business_schema import CreateBusinessDTO, ResponseBusinessDTO
from core.logger import get_scaly_logger
from api.deps.uow.infrastructure_uow import InfrastructureUnitOfWork
from api.deps import get_uow
from core.exceptions.exceptions import BusinessCreationFailedException, YouAreNotAllowedToAccessThisBusiness
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
        is_member = await uow.business_member_service.is_user_a_member_of_business(business_id, user_id=user.id)
        if not is_member:
            raise YouAreNotAllowedToAccessThisBusiness()
        business = await uow.business_service.get_business_by_id(business_id)
        return business


@router.get("/{business_id}/members", response_model=List[ResponseBusinessMemberDTO])
async def get_members_of_business(business_id: int, request: Request, uow: InfrastructureUnitOfWork = Depends(get_uow)):
    async with uow:
        clerk_id = request.state.user["sub"]
        user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
        is_member = await uow.business_member_service.is_user_a_member_of_business(business_id, user_id=user.id)
        if not is_member:
            raise YouAreNotAllowedToAccessThisBusiness()
        members = await uow.business_member_service.get_members_of_business(business_id)
        return members
