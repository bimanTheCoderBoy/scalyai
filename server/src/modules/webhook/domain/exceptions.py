from shared.base_exception import BaseAppException


class WebHookInvalidSignatureException(BaseAppException):
    def __init__(
        self,
        message: str = "Invalid signature",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class InvalidWebhookPayloadException(BaseAppException):
    def __init__(
        self,
        message: str = "Invalid webhook payload",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class WebhookEventAlreadyExistsException(BaseAppException):
    def __init__(
        self,
        message: str = "Webhook event already exists",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class WebhookEventCreationFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to create webhook event",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class WebhookEventUpdateFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to update webhook event",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class WebhookCacheError(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to access webhook cache",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class RedisClientNotInitializedError(BaseAppException):
    def __init__(
        self,
        message: str = "Redis client not initialized",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)
