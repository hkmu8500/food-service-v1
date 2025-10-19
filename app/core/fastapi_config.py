from fastapi import FastAPI

from app.api.api_router import api_router


def init_fastapi() -> FastAPI:
    app = FastAPI(
        title = "Vercel + FastAPI",
        description = "Vercel + FastAPI",
        version = "1.0.0",
        docs_url = "/api/docs",
        redoc_url = "/api/redoc",
        openapi_url = "/api/openapi.json",
    )

    app.include_router(api_router)
    return app
