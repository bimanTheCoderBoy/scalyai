from pydantic import BaseModel, Field
from typing import List
from models.business_user_mappings import BusinessUserRole

class BusinessUserDTO(BaseModel):
    name: str = Field(..., description="Name of the business")
    description: str = Field(..., description="Description of the business")
    industry: str = Field(..., description="Industry of the business")
    permissions: dict = Field(..., description="Permissions of the business")
    role: BusinessUserRole = Field(..., description="Role of the user in the business")

   