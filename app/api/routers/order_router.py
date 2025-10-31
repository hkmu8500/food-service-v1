from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.order_model import OrderModel, OrderStatusEnum
from app.persistence.repositories.order_repository import OrderRepository
from app.serivce.order_service import OrderService
from app.core.db_config import get_db_session
from app.models.schemas.base_response import BaseResponse
from app.models.schemas.order import Order
from app.models.schemas.order_create import OrderCreate
from app.models.schemas.Item import Item
from app.persistence.repositories.item_repository import ItemRepository
from app.serivce.item_service import ItemService
from app.models.convertor.OrderConvertor import order_model_to_order

router = APIRouter(prefix = "/api/orders", tags = ["Orders"])

def get_item_service(session: Session = Depends(get_db_session)) -> ItemService:
    """Dependency that provides ItemService instance"""
    repository = ItemRepository(session)
    return ItemService(repository)

def get_order_service(session: Session = Depends(get_db_session)) -> OrderService:
    """Dependency that provides OrderService instance"""
    repository = OrderRepository(session)
    return OrderService(repository)


@router.get("/{userId}", response_model = BaseResponse[list[OrderModel]])
def get_orders(userId: int, service: OrderService = Depends(get_order_service)) -> BaseResponse[list[OrderModel]]:
    """Get all orders for a user"""
    order_models = service.get_orders()
    orders = [order_model_to_order(o) for o in order_models if o.user_id == userId]
    return BaseResponse.create_success(data = orders)

@router.post("/{userId}", response_model = BaseResponse[Order])
def create_order(
    userId: int,
    payload: OrderCreate,
    service: OrderService = Depends(get_order_service),
    item_service: ItemService = Depends(get_item_service),
) -> BaseResponse[Order]:
    """Create a new order with selected items for a user"""
    created = service.create_order(user_id=userId, items=payload.items, fulfillment_type=payload.fulfillment_type, item_service=item_service)
    return BaseResponse.create_success(data = order_model_to_order(created))

