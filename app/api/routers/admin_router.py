from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models.schemas.base_response import BaseResponse
from app.core.db_config import drop_tables, create_tables
from app.utils.db_init import init_db
from app.serivce.order_service import OrderService, OrderRepository
from app.models.order_model import OrderModel
from app.core.db_config import get_db_session

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


@router.get("/orders", response_model = BaseResponse[list[OrderModel]])
def get_all_orders(service: OrderService = Depends(get_order_service)) -> BaseResponse[list[OrderModel]]:
    """Get all orders"""
    orders = service.get_orders()
    return BaseResponse.create_success(data = orders)