class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


#WebHook Exceptions

class WebHookInvalidSignatureException(BaseAppException):
    def __init__(self, message: str = "Invalid signature", status_code: int = 400):
        super().__init__(message, status_code)

