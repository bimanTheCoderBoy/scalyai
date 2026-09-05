from enum import IntEnum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class ResponseStatus(IntEnum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class ResponseSchema(BaseModel):
    status: ResponseStatus
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    errors: Optional[List[str]] = None
