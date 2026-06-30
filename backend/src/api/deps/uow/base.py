from sqlalchemy.ext.asyncio import AsyncSession
from db.session import AsyncSessionLocal


class BaseUnitOfWork:
    def __init__(self, session_factory=AsyncSessionLocal):
        self._session_factory = session_factory

    async def __aenter__(self):
        self.session: AsyncSession = self._session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
