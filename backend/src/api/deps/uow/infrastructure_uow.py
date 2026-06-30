from api.deps.uow.base import BaseUnitOfWork
from repositories.user_repository import UserRepository
from repositories.business_repository import BusinessRepository
from repositories.business_member_repository import BusinessMemberRepository
from services.user_service import UserService
from services.business_service import BusinessService
from services.business_member_service import BusinessMemberService


class InfrastructureUnitOfWork(BaseUnitOfWork):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._user_repo: UserRepository | None = None
        self._business_repo: BusinessRepository | None = None
        self._business_member_repo: BusinessMemberRepository | None = None
        self._user_service: UserService | None = None
        self._business_service: BusinessService | None = None
        self._business_member_service: BusinessMemberService | None = None

    @property
    def user_repo(self) -> UserRepository:
        if self._user_repo is None:
            self._user_repo = UserRepository(db=self.session)
        return self._user_repo

    @property
    def business_repo(self) -> BusinessRepository:
        if self._business_repo is None:
            self._business_repo = BusinessRepository(db=self.session)
        return self._business_repo

    @property
    def business_member_repo(self) -> BusinessMemberRepository:
        if self._business_member_repo is None:
            self._business_member_repo = BusinessMemberRepository(db=self.session)
        return self._business_member_repo

    @property
    def user_service(self) -> UserService:
        if self._user_service is None:
            self._user_service = UserService(user_repo=self.user_repo)
        return self._user_service

    @property
    def business_service(self) -> BusinessService:
        if self._business_service is None:
            self._business_service = BusinessService(
                business_repo=self.business_repo,
                business_member_repo=self.business_member_repo,
            )
        return self._business_service

    @property
    def business_member_service(self) -> BusinessMemberService:
        if self._business_member_service is None:
            self._business_member_service = BusinessMemberService(
                business_member_repo=self.business_member_repo,
                business_repo=self.business_repo,
                user_repo=self.user_repo,
            )
        return self._business_member_service
