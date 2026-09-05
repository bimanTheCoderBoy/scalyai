from abc import ABC, abstractmethod



class PushDBPubSubRepositoryInterface(ABC):
    @abstractmethod
    async def publish(self, channel: str, message: str) -> None:
        pass

    # @abstractmethod
    # async def subscribe(self, channel: str) -> None:
    #     pass

    # @abstractmethod
    # async def unsubscribe(self, channel: str) -> None:
    #     pass
