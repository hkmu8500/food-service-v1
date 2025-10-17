from fastapi import FastAPI


app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

from app.api.main import api_router

app.include_router(api_router)