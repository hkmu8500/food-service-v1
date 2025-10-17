from fastapi import FastAPI

from app.api.api_router import api_router
from .core.exception_handlers import register_exception_handlers

app = FastAPI(
    title = "Vercel + FastAPI",
    description = "Vercel + FastAPI",
    version = "1.0.0",
)

# Register the exception handler
register_exception_handlers(app)

app.include_router(api_router)
