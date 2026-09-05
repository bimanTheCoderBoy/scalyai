from shared.base_exception import BaseAppException


class BusinessDeletionFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to delete business",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessAlreadyExistsException(BaseAppException):
    def __init__(
        self,
        message: str = "Business already exists",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class BusinessNotFoundException(BaseAppException):
    def __init__(
        self,
        message: str = "Business not found",
        status_code: int = 404,
    ):
        super().__init__(message, status_code)


class SameValueAlreadyExists(BaseAppException):
    def __init__(
        self,
        message: str = "Business with same value already exists",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessCreationFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to create business",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessUpdateDetailsPatchFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to update business details",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessMemberAlreadyExistsException(BaseAppException):
    def __init__(
        self,
        message: str = "Business member already exists",
        status_code: int = 400,
    ):
        super().__init__(message, status_code)


class BusinessMemberNotFoundException(BaseAppException):
    def __init__(
        self,
        message: str = "Business member not found",
        status_code: int = 404,
    ):
        super().__init__(message, status_code)


class BusinessMemberAdditionFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to add business member",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class YouAreNotAllowedToAccessThisBusiness(BaseAppException):
    def __init__(
        self,
        message: str = "You are not a allowed to access this business",
        status_code: int = 403,
    ):
        super().__init__(message, status_code)


class BusinessMemberDeletionFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to delete business member",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)


class BusinessMemberUpdateFailedException(BaseAppException):
    def __init__(
        self,
        message: str = "Failed to update business member",
        status_code: int = 500,
    ):
        super().__init__(message, status_code)
