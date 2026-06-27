from pydantic import BaseModel, Field
from typing import List
from models.business_user_mappings import BusinessUserRole
from datetime import datetime
class BusinessUserDTO(BaseModel):
    name: str = Field(..., description="Name of the business")
    description: str = Field(..., description="Description of the business")
    industry: str = Field(..., description="Industry of the business")
    permissions: dict = Field(..., description="Permissions of the business")
    role: BusinessUserRole = Field(..., description="Role of the user in the business")
    
class ResponseBusinessDTO(BaseModel):
    id: int = Field(..., description="ID of the business")
    name: str = Field(..., description="Name of the business")
    description: str = Field(..., description="Description of the business")
    industry: str = Field(..., description="Industry of the business")
    created_at: datetime = Field(..., description="Created at")
    updated_at: datetime = Field(..., description="Updated at")

class CreateBusinessDTO(BaseModel):
    name: str = Field(..., description="Name of the business")
    description: str = Field(..., description="Description of the business")
    industry: str = Field(..., description="Industry of the business")

class ResponseBusinessMemberDTO(BaseModel):
    name: str = Field(..., description="Name of the member")
    email: str = Field(..., description="Email of the member")
    role: BusinessUserRole = Field(..., description="Role of the member")
    permissions: dict = Field(..., description="Permissions of the member")
   
    


