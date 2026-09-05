from pydantic import BaseModel, Field
from models.business_invites import BusinessUserRole, BusinessInviteStatus
from datetime import datetime
class BusinessInviteRequestSchema(BaseModel):
    business_id: int = Field(..., description="The ID of the business to invite the user to")
    to_user_id: int = Field(..., description="The ID of the user receiving the invitation")
    role: BusinessUserRole = Field(..., description="The role of the user receiving the invitation")

class BusinessInviteCreateSchema(BaseModel):
    business_id: int = Field(..., description="The ID of the business to invite the user to")
    from_user_id: int = Field(..., description="The ID of the user sending the invitation")
    to_user_id: int = Field(..., description="The ID of the user receiving the invitation")
    role: BusinessUserRole = Field(..., description="The role of the user receiving the invitation")
    
class BusinessInviteResponseSchema(BusinessInviteCreateSchema):
    id: int = Field(..., description="The ID of the invitation")
    status: BusinessInviteStatus = Field(..., description="The status of the invitation")
    created_at: datetime = Field(..., description="The date and time the invitation was created")
    updated_at: datetime = Field(..., description="The date and time the invitation was last updated")
    class Config:
        from_attributes = True

# class BusinessInviteAcceptSchema(BaseModel):
