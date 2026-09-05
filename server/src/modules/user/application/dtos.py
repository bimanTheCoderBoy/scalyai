from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    email: Optional[str] = Field(None, description="Email of the user")


class CurrentUser(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    email: Optional[str] = Field(None, description="Email of the user")


class UserFullDetailsDTO(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    email: Optional[str] = Field(None, description="Email of the user")
    updated_at: datetime = Field(..., description="Updated at")
    created_at: datetime = Field(..., description="Created at")


class UserPatchResponseDTO(BaseModel):
    id: int = Field(..., description="ID of the user")
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    email: Optional[str] = Field(None, description="Email of the user")
    updated_at: datetime = Field(..., description="Updated at")
    created_at: datetime = Field(..., description="Created at")


class UserPatchDTO(BaseModel):
    name: Optional[str] = Field(None, description="Name of the user")
    email: Optional[str] = Field(None, description="Email of the user")
