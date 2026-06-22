from dotenv import load_dotenv
import os
load_dotenv()


#Check if all the env variables are set
#list of env variables to check
# env_variables = ["DATABASE_URL", "REDIS_PORT"]
# if not all(os.getenv(var) for var in env_variables):
#     raise ValueError(f"Missing environment variables: {', '.join(env_variables)}")



class DatabaseConfig:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "")

class RedisConfig:
    def __init__(self):
        self.REDIS_PORT = os.getenv("REDIS_PORT", "")

class ClerkConfig:
    def __init__(self) -> None:
        self.CLERK_ISSUER = os.getenv("CLERK_ISSUER", "")
        self.CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET", "")
        self.CLERK_PUBLIC_KEY_URL = f"{self.CLERK_ISSUER}/.well-known/jwks.json"

class SecurityConfig:
    def __init__(self) -> None:
        self.PUBLIC_PATHS = {
            "/webhooks/clerk/",
            "/health",
        }

#singletone 
database_config = DatabaseConfig()
redis_config = RedisConfig()
clerk_config = ClerkConfig()
security_config = SecurityConfig()