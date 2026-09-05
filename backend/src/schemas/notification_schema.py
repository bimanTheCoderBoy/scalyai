from pydantic import BaseModel, Field
from datetime import datetime
from models.notifications import NotificationType
from typing import Optional

class NotificationMessageTemplate(BaseModel):
    title: str = Field(..., description="The title of the notification")
    message: str = Field(..., description="The message of the notification")
    
class NotificationCreateSchema(BaseModel):
    user_id: int = Field(..., description="The ID of the user to send the notification to")
    title: str = Field(..., description="The title of the notification")
    message: str = Field(..., description="The message of the notification")
    type: NotificationType = Field(..., description="The type of the notification")
    extra_data: Optional[dict] = Field(default=None, description="The extra data of the notification")

class NotificationResponseSchema(NotificationCreateSchema):
    id: int = Field(..., description="The ID of the notification")
    created_at: datetime = Field(..., description="The date and time the notification was created")
    updated_at: datetime = Field(..., description="The date and time the notification was last updated")
    class Config:
        from_attributes = True
