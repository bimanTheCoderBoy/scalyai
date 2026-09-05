from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import database_config
DATABASE_URL = database_config.DATABASE_URL
from contextlib import asynccontextmanager

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

worker_engine = create_async_engine(
    DATABASE_URL,
    # echo=True,
    pool_size=2,
    max_overflow=3,
    pool_timeout=30,
    pool_pre_ping=True
   )

@asynccontextmanager
async def worker_session_factory():
    
    session_maker = async_sessionmaker[AsyncSession](
        worker_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False
    )
    async with session_maker() as session:
        try:
            yield session
        finally:
            await session.close()