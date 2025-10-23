from fastapi import APIRouter

from app.api.routers.item_router import router as items_router
from app.api.routers.user_router import router as user_router
from app.api.routers.order_router import router as order_router

api_router = APIRouter()
api_router.include_router(items_router)
api_router.include_router(user_router)
api_router.include_router(order_router)
