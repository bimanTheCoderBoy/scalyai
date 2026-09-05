from modules.notification.infrastructure.adapters.pubsub_interface import (
    PushDBPubSubRepositoryInterface,
)


class RedisPubSubRepository(PushDBPubSubRepositoryInterface):
    async def publish(self, channel: str, message: str) -> None:
        ...
