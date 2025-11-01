from fastapi import APIRouter, Depends, Header
from sqlmodel import Session
from app.models.schemas.base_response import BaseResponse
from app.core.db_config import drop_tables, create_tables
from app.utils.db_init import init_db
from app.serivce.order_service import OrderService, OrderRepository
from app.models.order_model import OrderModel
from app.core.db_config import get_db_session
from app.models.convertor.OrderConvertor import order_model_to_order
from app.models.schemas.order import Order, OrderStatusEnum



router = APIRouter(prefix = "/api/admin", tags = ["Admin"])

def get_order_service(session: Session = Depends(get_db_session)) -> OrderService:
    """Dependency that provides OrderService instance"""
    repository = OrderRepository(session)
    return OrderService(repository)

@router.post("/table/refreshAll", response_model = BaseResponse[None])
def table_refresh_all() -> BaseResponse[None]:
    """Refresh all database tables"""
    drop_tables()
    create_tables()
    init_db()
    return BaseResponse.create_success(message = "Tables refreshed successfully", data = None)


@router.get("/orders", response_model = BaseResponse[list[Order]])
def get_all_orders(
    X_Admin_Name: str | None = Header(None, alias="X-Admin-Name"),
    service: OrderService = Depends(get_order_service)) -> BaseResponse[list[Order]]:
    """Get all orders"""
    if X_Admin_Name != "admin":
        return BaseResponse.create_error(message = "Forbidden", data = None)

    order_models = service.get_orders()
    orders = [order_model_to_order(o) for o in order_models]
    return BaseResponse.create_success(data = orders)

@router.post("/orders/{order_id}/status", response_model = BaseResponse[None])
def update_order_status(order_id: int, status: OrderStatusEnum, service: OrderService = Depends(get_order_service)) -> BaseResponse[None]:
    """Update order status"""
    service.update_order_status(order_id, status)
    return BaseResponse.create_success(message = "Order status updated successfully", data = None)
