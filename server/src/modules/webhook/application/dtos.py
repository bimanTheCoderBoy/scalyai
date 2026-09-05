from datetime import datetime
from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel, Field


class WebhookEventStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class WebhookEventDTO(BaseModel):
    event_id: str = Field(..., description="Unique webhook event id")
    type: str = Field(..., description="Webhook event type")
    event_timestamp: datetime = Field(
        ..., description="Timestamp of the event"
    )
    event_status: WebhookEventStatus = Field(
        default=WebhookEventStatus.PENDING,
        description="Current processing status of webhook event",
    )
    data: Dict[str, Any] = Field(
        default_factory=dict, description="Webhook payload data"
    )
