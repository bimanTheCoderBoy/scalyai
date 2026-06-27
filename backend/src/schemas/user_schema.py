from pydantic import BaseModel, Field
from schemas.business_schema import BusinessUserDTO
from typing import List

class UserDTO(BaseModel):
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: str = Field(None, description="Name of the user")
    email: str = Field(..., description="Email of the user")

class UserAndBusinessDTO(BaseModel):
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email of the user")
    business: List[BusinessUserDTO] = Field(..., description="Businesses of the user")      