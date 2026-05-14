from dotenv import load_dotenv
import os
load_dotenv()


#Check if all the env variables are set
#list of env variables to check
# env_variables = ["DATABASE_URL", "REDIS_PORT", "CLERK_WEBHOOK_SECRET", "CELERY_BROKER_URL", "CELERY_RESULT_BACKEND"]
# if not all(os.getenv(var) for var in env_variables):
#     raise ValueError(f"Missing environment variables: {', '.join(env_variables)}")



class DatabaseConfig:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "")

class RedisConfig:
    def __init__(self):
        self.REDIS_PORT = os.getenv("REDIS_PORT", "")
        self.REDIS_DB = os.getenv("REDIS_DB", "")
        self.REDIS_HOST = os.getenv("REDIS_HOST", "")


class ClerkConfig:
    def __init__(self):
        self.CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET", "")


class CeleryConfig:
    def __init__(self):
        self.CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "")
        self.CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "")
#singletone 
database_config = DatabaseConfig()
redis_config = RedisConfig()
clerk_config = ClerkConfig()
celery_config = CeleryConfig()