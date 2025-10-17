from fastapi import APIRouter
from app.api.routers.items import router as items_router


api_router = APIRouter()
api_router.include_router(items_router)