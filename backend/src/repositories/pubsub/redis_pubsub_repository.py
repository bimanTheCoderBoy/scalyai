from interfaces.pubsub_interface import PushDBPubSubRepositoryInterface


class RedisPubSubRepository(PushDBPubSubRepositoryInterface):
    def publish(self, channel: str, message: str) -> None:
         ...