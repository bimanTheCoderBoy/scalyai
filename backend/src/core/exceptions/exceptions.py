class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


#WebHook Exceptions

class WebHookInvalidSignatureException(BaseAppException):
    def __init__(self, message: str = "Invalid signature", status_code: int = 400):
        super().__init__(message, status_code)

class InvalidWebhookPayloadException(BaseAppException):
    def __init__(self, message: str = "Invalid webhook payload", status_code: int = 400):
        super().__init__(message, status_code)

class WebhookEventAlreadyExistsException(BaseAppException):
    def __init__(self, message: str = "Webhook event already exists", status_code: int = 400):
        super().__init__(message, status_code)

class WebhookEventCreationFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to create webhook event", status_code: int = 500):
        super().__init__(message, status_code)
class WebhookEventUpdateFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to update webhook event", status_code: int = 500):
        super().__init__(message, status_code)
class WebhookCacheError(BaseAppException):
    def __init__(self, message: str = "Failed to access webhook cache", status_code: int = 500):
        super().__init__(message, status_code)
class RedisClientNotInitializedError(BaseAppException):
    def __init__(self, message: str = "Redis client not initialized", status_code: int = 500):
        super().__init__(message, status_code)
#User Exceptions
class UserCreationFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to create user", status_code: int = 500):
        super().__init__(message, status_code)
class UserAlreadyExistsException(BaseAppException):
    def __init__(self, message: str = "User already exists", status_code: int = 400):
        super().__init__(message, status_code)
class UserNotFoundException(BaseAppException):
    def __init__(self, message: str = "User not found", status_code: int = 404):
        super().__init__(message, status_code)