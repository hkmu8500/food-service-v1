from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .schemas import BaseResponse  # Import our base response model


async def global_exception_handler(request: Request, exc: Exception):
    """
    A global exception handler to catch any unhandled exceptions and return a consistent error response.
    """
    # You can log the detailed exception 'exc' here for debugging purposes.
    return JSONResponse(
        status_code = 500,
        content = BaseResponse.error(message = "Internal server error").model_dump()
    )


def register_exception_handlers(app: FastAPI):
    """Register the global exception handler."""
    app.add_exception_handler(Exception, global_exception_handler)
