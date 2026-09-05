from modules.user.application.user_service import UserService
from modules.user.infrastructure.user_repository import UserRepository
from modules.webhook.application.event_handling.clerk_user_handler import (
    ClerkUserHandler,
)
from modules.webhook.application.webhook_service import WebhookEventService
from modules.webhook.infrastructure.webhook_repository import WebhookRepository
from shared.uow import BaseUnitOfWork


class WebhookWorkerUnitOfWork(BaseUnitOfWork):
    def __init__(self):
        super().__init__()
        self._webhook_repo: WebhookRepository | None = None
        self._user_repo: UserRepository | None = None
        self._event_service: WebhookEventService | None = None
        self._user_service: UserService | None = None
        self._clerk_handler: ClerkUserHandler | None = None

    @property
    def webhook_repo(self) -> WebhookRepository:
        if self._webhook_repo is None:
            self._webhook_repo = WebhookRepository(db=self.session)
        return self._webhook_repo

    @property
    def user_repo(self) -> UserRepository:
        if self._user_repo is None:
            self._user_repo = UserRepository(db=self.session)
        return self._user_repo

    @property
    def event_service(self) -> WebhookEventService:
        if self._event_service is None:
            self._event_service = WebhookEventService(event_repo=self.webhook_repo)
        return self._event_service

    @property
    def user_service(self) -> UserService:
        if self._user_service is None:
            self._user_service = UserService(user_repo=self.user_repo)
        return self._user_service

    @property
    def clerk_handler(self) -> ClerkUserHandler:
        if self._clerk_handler is None:
            self._clerk_handler = ClerkUserHandler(user_service=self.user_service)
        return self._clerk_handler
