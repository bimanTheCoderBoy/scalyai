from abc import ABC, abstractmethod


class PushDBPubSubRepositoryInterface(ABC):
    @abstractmethod
    async def publish(self, channel: str, message: str) -> None:
        pass
