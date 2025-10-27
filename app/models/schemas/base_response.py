from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

# Generic type variable for the actual data type in the response
T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    """
    A base response model for all API endpoints to ensure consistent structure.
    """
    success: bool
    message: str
    data: Optional[T] = None  # The actual response data, optional for error cases

    # Example class method for a successful response
    @classmethod
    def create_success(cls, data: T, message: str = "Success") -> "BaseResponse[T]":
        return cls(success = True, message = message, data = data)

    # Example class method for an error response
    @classmethod
    def create_error(cls, message: str, data: Optional[T] = None) -> "BaseResponse[None]":
        return cls(success = False, message = message, data = data)
