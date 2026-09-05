from shared.base_exception import BaseAppException


class NotificationCreationFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to create notification",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class NotificationGetFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to get notification",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)
