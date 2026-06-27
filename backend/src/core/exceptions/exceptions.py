

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
class UserGetFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to get user", status_code: int = 500):
        super().__init__(message, status_code)
class UserPatchFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to patch user", status_code: int = 500):
        super().__init__(message, status_code)
class NoPatchDataFoundException(BaseAppException):
    def __init__(self, message: str = "No patch data found", status_code: int = 400):
        super().__init__(message, status_code)

#Business Exceptions4

class BusinessDeletionFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to delete business", status_code: int = 500):
        super().__init__(message, status_code)
class BusinessAlreadyExistsException(BaseAppException):
    def __init__(self, message: str = "Business already exists", status_code: int = 400):
        super().__init__(message, status_code)

class BusinessNotFoundException(BaseAppException):
    def __init__(self, message: str = "Business not found", status_code: int = 404):
        super().__init__(message, status_code)

class SameValueAlreadyExists(BaseAppException):
    def __init__(self, message: str = "Business with same value already exists", status_code: int = 500):
        super().__init__(message, status_code)
class BusinessCreationFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to create business", status_code: int = 500):
        super().__init__(message, status_code)


#Business Member Exceptions
class BusinessMemberAlreadyExistsException(BaseAppException):
    def __init__(self, message: str = "Business member already exists", status_code: int = 400):
        super().__init__(message, status_code)
class BusinessMemberNotFoundException(BaseAppException):
    def __init__(self, message: str = "Business member not found", status_code: int = 404):
        super().__init__(message, status_code)
class BusinessMemberAdditionFailedException(BaseAppException):
    def __init__(self, message: str = "Failed to add business member", status_code: int = 500):
        super().__init__(message, status_code)

class YouAreNotAllowedToAccessThisBusiness(BaseAppException):
    def __init__(self, message: str = "You are not a allowed to access this business", status_code: int = 403):
        super().__init__(message, status_code)