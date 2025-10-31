from typing import List
from app.models.order_model import OrderModel
from app.models.order_item import OrderItemModel
from app.models.schemas.order import Order
from app.models.schemas.order_item import OrderItem
from app.models.convertor.ItemConvertor import item_model_to_item


def order_model_to_order(db_order: OrderModel) -> Order:
    """Convert SQLModel OrderModel (with items) to Pydantic Order"""
    items: List[OrderItem] = []
    if db_order.items:
        for oi in db_order.items:
            # oi: OrderItemModel
            item_schema = item_model_to_item(oi.item) if oi.item is not None else None
            items.append(
                OrderItem(
                    id=oi.id,
                    quantity=oi.quantity,
                    item=item_schema,
                    price=oi.price,
                )
            )

    return Order(
        user_id=db_order.user_id,
        total_price=db_order.total_price,
        status=db_order.status,
        fulfillment_type=db_order.fulfillment_type.value,
        items=items,
    )