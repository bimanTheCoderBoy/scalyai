from db import Base, BaseModelMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from enum import Enum

class NotificationType(Enum):
    INVITATION = "invitation"
    MESSAGE = "message"
    EVENT = "event"
    OTHER = "other"

class Notification(BaseModelMixin,Base):
    __tablename__ = "notifications"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    # is_read: Mapped[bool]= mapped_column(Boolean, default=False)
    extra_data: Mapped[dict] = mapped_column(JSON, default={})
    type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), nullable=False)
    
    #Relations
    user=relationship('User', back_populates='notifications')
