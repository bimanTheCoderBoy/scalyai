from shared.base_exception import BaseAppException


class BusinessInviteAlreadyExistsException(BaseAppException):
    def __init__(
        self,
        message: str = "Business invite already exists",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class BusinessInviteNotFoundException(BaseAppException):
    def __init__(
        self,
        message: str = "Business invite not found",
        status_code: int = 404,
    ):
        super().__init__(message, status_code)


class BusinessInviteCreationFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to create business invite",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessInviteAcceptanceFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to accept business invite",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessInviteRejectionFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to reject business invite",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessInviteCancellationFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to cancel business invite",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)
