from pydantic import BaseModel, Field
from schemas.business_schema import BusinessUserDTO
from typing import List
from datetime import datetime
class UserDTO(BaseModel):
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: str = Field(None, description="Name of the user")
    email: str = Field(..., description="Email of the user")

class CurrentUser(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email of the user")

class UserFullDetailsDTO(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user") 
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email of the user")
    updated_at: datetime = Field(..., description="Updated at")
    created_at: datetime = Field(..., description="Created at")  

class UserPatchResponseDTO(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user") 
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email of the user")
    updated_at: datetime = Field(..., description="Updated at")
    created_at: datetime = Field(..., description="Created at")  

class UserPatchDTO(BaseModel):
    name: str = Field(None, description="Name of the user")
    email: str = Field(None, description="Email of the user")