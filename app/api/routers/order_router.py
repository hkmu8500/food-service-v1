from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.order_model import OrderModel, OrderStatusEnum
from app.persistence.repositories.order_repository import OrderRepository
from app.serivce.order_service import OrderService
from app.core.db_config import get_db_session
from app.models.schemas.base_response import BaseResponse
from app.models.schemas.order import Order

router = APIRouter(prefix = "/api/orders", tags = ["Orders"])


def get_order_service(session: Session = Depends(get_db_session)) -> OrderService:
    """Dependency that provides OrderService instance"""
    repository = OrderRepository(session)
    return OrderService(repository)


@router.get("/", response_model = BaseResponse[list[Order]])
def get_orders(service: OrderService = Depends(get_order_service)) -> BaseResponse[list[Order]]:
    """Get all orders"""
    orders = service.get_orders()
    return BaseResponse.create_success(data = orders)


