from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from app.models.order_model import OrderModel, OrderStatusEnum
from app.persistence.repositories.order_repository import OrderRepository
from app.serivce.order_service import OrderService
from app.core.db_config import get_db_session
from app.models.schemas.base_response import BaseResponse
from app.models.schemas.order import Order
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix = "/api/orders", tags = ["Orders"])


def get_order_service(session: Session = Depends(get_db_session)) -> OrderService:
    """Dependency that provides OrderService instance"""
    repository = OrderRepository(session)
    return OrderService(repository)


@router.get("/", response_model = BaseResponse[list[Order]])
def get_orders(request: Request, service: OrderService = Depends(get_order_service)) -> BaseResponse[list[Order]]:
    """Get all orders (filtered by session user when available)."""
    user = request.session.get("user") or {}
    user_id = user.get("id")
    user_name = user.get("name")

    if user_id is None:
        logger.warning("Get orders requested without session user")
        orders = []
    else:
        logger.info("Get orders for user_id=%s user_name=%s", user_id, user_name)
        orders = service.get_orders_by_filters(user_id)

    return BaseResponse.create_success(data = orders)


