import threading

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config.settings import database_config
from shared.logger import get_scaly_logger

logger = get_scaly_logger(name=__name__)


class Database:
    _instance: "Database | None" = None
    _engine: AsyncEngine | None = None
    _session_factory: async_sessionmaker[AsyncSession] | None = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> "Database":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def engine(self) -> AsyncEngine:
        if self._engine is None:
            with self._lock:
                if self._engine is None:
                    self._engine = create_async_engine(
                        database_config.DATABASE_URL,
                        echo=True,
                        pool_size=10,
                        max_overflow=20,
                        pool_timeout=30,
                        pool_recycle=1800,
                        pool_pre_ping=True,
                    )
                    logger.info("Database engine created.")
        return self._engine

    @property
    def session_factory(self) -> async_sessionmaker[AsyncSession]:
        if self._session_factory is None:
            with self._lock:
                if self._session_factory is None:
                    self._session_factory = async_sessionmaker(
                        self.engine,
                        class_=AsyncSession,
                        expire_on_commit=False,
                        autoflush=False,
                    )
        return self._session_factory

    async def close(self):
        if self._engine is not None:
            await self._engine.dispose()
            self._engine = None
            self._session_factory = None
            logger.info("Database engine disposed.")


db = Database()


async def init_db():
    from shared.base_entity import Base

    try:
        logger.info("Starting database initialization...")
        async with db.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("All tables created successfully...")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        from shared.base_exception import BaseAppException

        raise BaseAppException("Failed to initialize database", status_code=500)
