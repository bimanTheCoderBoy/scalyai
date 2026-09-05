from shared.base_exception import BaseAppException


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
