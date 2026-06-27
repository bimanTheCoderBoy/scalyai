from api.deps.uow.base import BaseUnitOfWork
from repositories.user_repository import UserRepository
from services.user_service import UserService

class UserUnitOfWork(BaseUnitOfWork):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._user_repo: UserRepository | None = None
        self._user_service: UserService | None = None


    @property
    def user_repo(self) -> UserRepository:
        if self._user_repo is None:
            self._user_repo = UserRepository(db=self.session)
        return self._user_repo

    @property
    def user_service(self) -> UserService:
        if self._user_service is None:
            self._user_service = UserService(user_repo=self.user_repo)
        return self._user_service
