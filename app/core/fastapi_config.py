from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.api_router import api_router
from app.core.db_config import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event logic here
    create_tables()
    print("Application created tables...")
    yield
    # Shutdown event logic here
    print("Application shutting down...")

def init_fastapi() -> FastAPI:
    app = FastAPI(
        lifespan = lifespan,
        title = "Vercel + FastAPI",
        description = "Vercel + FastAPI",
        version = "1.0.0",
        docs_url = "/api/docs",
        redoc_url = "/api/redoc",
        openapi_url = "/api/openapi.json",
    )

    app.include_router(api_router)
    return app
