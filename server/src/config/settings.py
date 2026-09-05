from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConfig:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "")


class RedisConfig:
    def __init__(self):
        self.REDIS_PORT = os.getenv("REDIS_PORT", "")
        self.REDIS_DB = os.getenv("REDIS_DB", "")
        self.REDIS_HOST = os.getenv("REDIS_HOST", "")


class ClerkConfig:
    def __init__(self) -> None:
        self.CLERK_ISSUER = os.getenv("CLERK_ISSUER", "")
        self.CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET", "")
        self.CLERK_PUBLIC_KEY_URL = f"{self.CLERK_ISSUER}/.well-known/jwks.json"


class SecurityConfig:
    def __init__(self) -> None:
        self.PRIVATE_PATHS = {
            "/api/v1/me",
            "/api/v1/business",
        }


class TaskIQConfig:
    def __init__(self):
        self.TASKIQ_BROKER_URL = os.getenv("TASKIQ_BROKER_URL", "")
        self.TASKIQ_RESULT_BACKEND = os.getenv("TASKIQ_RESULT_BACKEND", "")
        self.TASKIQ_BACKEND_TTL=int(os.getenv("TASKIQ_BACKEND_TTL", "3600"))

database_config = DatabaseConfig()
redis_config = RedisConfig()
clerk_config = ClerkConfig()
security_config = SecurityConfig()
taskiq_config = TaskIQConfig()