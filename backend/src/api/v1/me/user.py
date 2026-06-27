from fastapi import APIRouter
from schemas.user_schema import UserAndBusinessDTO
from fastapi import Request, Depends
from api.deps.uow.user_uow import UserUnitOfWork
from api.deps import get_user_uow
from core.exceptions.exceptions import UserGetFailedException

router = APIRouter(prefix="/me", tags=["users"])

@router.get("/", response_model=UserAndBusinessDTO)
async def get_me(request: Request, uow: UserUnitOfWork = Depends(get_user_uow)):
    clerk_id = request.state.user["sub"]
    async with uow:
        user_and_business: UserAndBusinessDTO = await uow.user_service.get_user_and_business_by_clerk_id(clerk_id)
        try:
            await uow.commit()
        except Exception:
            await uow.rollback()
            raise UserGetFailedException()
    return user_and_business

# @router.put("/")
# async def update_me(current_user: User = Depends(get_current_user)):