import enum
from datetime import datetime

from sqlalchemy import JSON, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from shared.base_entity import Base, BaseModelMixin


class WebhookEventStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class WebhookEvent(BaseModelMixin, Base):
    __tablename__ = "webhook_events"

    event_id: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True, index=True
    )
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    event_timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    event_status: Mapped[enum.Enum] = mapped_column(
        Enum(WebhookEventStatus),
        nullable=False,
        default=WebhookEventStatus.PENDING,
    )
    data: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
