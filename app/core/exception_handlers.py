from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
from app.models.schemas.base_response import BaseResponse


async def global_exception_handler(request: Request, exc: Exception):
    """
    A global exception handler to catch any unhandled exceptions and return a consistent error response.
    """
    # You can log the detailed exception 'exc' here for debugging purposes.
    traceback_list = traceback.format_exc().split("\n")
    return JSONResponse(
        status_code=500,
        content=BaseResponse.create_error(message=str(exc), data=traceback_list).model_dump()
    )


def register_exception_handlers(app: FastAPI):
    """Register the global exception handler."""
    app.add_exception_handler(Exception, global_exception_handler)
