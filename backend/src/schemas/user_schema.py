from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    clerk_id: str = Field(..., description="Clerk ID of the user")
    name: str = Field(None, description="Name of the user")
    email: str = Field(..., description="Email of the user")
    