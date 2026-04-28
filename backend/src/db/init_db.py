from db.base import Base
from db.session import engine
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)
from sqlalchemy import text
from core.exceptions import BaseAppException



async def init_db():
    try:
        logger.info("Starting database initialization...")

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        logger.info("All tables created successfully...")

    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise BaseAppException("Failed to initialize database", status_code=500)