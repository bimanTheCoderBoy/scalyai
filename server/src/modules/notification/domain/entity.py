from enum import Enum

from sqlalchemy import JSON, Enum as SAEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.base_entity import Base, BaseModelMixin


class NotificationType(Enum):
    INVITATION = "invitation"
    MESSAGE = "message"
    EVENT = "event"
    OTHER = "other"


class Notification(BaseModelMixin, Base):
    __tablename__ = "notifications"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    extra_data: Mapped[dict] = mapped_column(JSON, default={})
    type: Mapped[NotificationType] = mapped_column(
        SAEnum(NotificationType), nullable=False
    )

    user = relationship("User", back_populates="notifications")
