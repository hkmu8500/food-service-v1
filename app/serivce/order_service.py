from typing import List
from app.models.order_model import OrderModel, OrderStatusEnum, FulfillmentTypeEnum
from app.models.order_item import OrderItemModel
from app.persistence.repositories.order_repository import OrderRepository
from app.serivce.item_service import ItemService
from app.models.schemas.order_create import OrderCreateItem


class OrderService:
    """Service for OrderModel"""
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, user_id: int, user_name: str, items: List[OrderCreateItem], fulfillment_type: FulfillmentTypeEnum, item_service: ItemService) -> OrderModel:
        """Create a new order with selected items and userId"""
        order = OrderModel(
            user_id=user_id,
            user_name=user_name,    
            total_price=0.0,
            status=OrderStatusEnum.PENDING,
            fulfillment_type=fulfillment_type.value,
        )

        order_items: List[OrderItemModel] = []
        total = 0.0
        for payload in items:
            item = item_service.get_item(payload.menuId)
            if item is None:
                raise ValueError(f"Item {payload.menuId} not found")
            if not item.available:
                raise ValueError(f"Item {item.name} is not available")

            line_total = float(item.price) * payload.quantity
            total += line_total

            order_items.append(
                OrderItemModel(
                    item_id=item.id,
                    quantity=payload.quantity,
                    price=float(item.price),
                    total_price=line_total,
                )
            )

        order.total_price = total
        order.items = order_items

        return self.repository.create_order(order)

    def get_orders(self) -> list[OrderModel]:
        """Get all orders"""
        return self.repository.get_orders()

    def update_order_status(self, order_id: str, status: str) -> None:
        """Update order status"""
        # load the entity from the database, and modify the status
        order = self.repository.get_order(order_id)
        if order is None:
            raise ValueError(f"Order {order_id} not found")
        order.status = OrderStatusEnum(status)
        self.repository.update_order(order)