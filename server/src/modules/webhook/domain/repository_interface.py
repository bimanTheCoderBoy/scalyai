from abc import ABC, abstractmethod
from typing import Optional

from modules.webhook.domain.entity import WebhookEvent, WebhookEventStatus


class IWebhookRepository(ABC):
    @abstractmethod
    async def create(self, event: WebhookEvent) -> WebhookEvent:
        pass

    @abstractmethod
    async def get_by_event_id(self, event_id: str) -> Optional[WebhookEvent]:
        pass

    @abstractmethod
    async def update_event_status(
        self, event_id: str, status: WebhookEventStatus
    ) -> str:
        pass


class IWebhookCacheRepository(ABC):
    @abstractmethod
    async def is_duplicate(self, event_id: str) -> bool:
        pass

    @abstractmethod
    async def mark_processed(self, event_id: str) -> None:
        pass

    @abstractmethod
    async def remove(self, event_id: str) -> None:
        pass
