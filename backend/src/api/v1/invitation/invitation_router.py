from fastapi import APIRouter, Request
from schemas.invitation_schema import BusinessInviteResponseSchema, BusinessInviteRequestSchema, BusinessInviteCreateSchema
from core.logger import get_scaly_logger
from api.deps.uow.infrastructure_uow import InfrastructureUnitOfWork
from fastapi import Depends
from core.exceptions.exceptions import BusinessInviteCreationFailedException, UserNotFoundException
logger = get_scaly_logger(name=__name__)

router = APIRouter(prefix="/invitations", tags=["invitations"])
@router.post("/", response_model=BusinessInviteResponseSchema)
async def create_invitation(invitation: BusinessInviteRequestSchema, request: Request, uow: InfrastructureUnitOfWork = Depends(InfrastructureUnitOfWork)):
    async with uow:
      clerk_id = request.state.user["sub"]
      user = await uow.user_service.get_user_by_clerk_id(clerk_id=clerk_id)
      if user is None:
        raise UserNotFoundException()

      invitation = BusinessInviteCreateSchema(
        business_id=invitation.business_id,
        from_user_id=user.id,
        to_user_id=invitation.to_user_id,
        role=invitation.role
      )
      response_invitation = await uow.invitation_service.send_invitation(invitation)
      try:
        await uow.commit()
        return response_invitation
      except Exception as e:
        await uow.rollback()
        logger.error(f"Error creating invitation: {e}")
        raise BusinessInviteCreationFailedException()
  
