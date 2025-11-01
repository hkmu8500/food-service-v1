from typing import List
from app.models.order_model import OrderModel
from app.models.order_item import OrderItemModel
from app.models.schemas.order import Order
from app.models.schemas.order_item import OrderItem


def order_model_to_order(db_order: OrderModel) -> Order:
    """Convert SQLModel OrderModel (with items) to Pydantic Order"""
    items: List[OrderItem] = []
    print("the length of items", len(db_order.items))
    if db_order.items:
        for oi in db_order.items:
            # oi: OrderItemModel
            items.append(
                OrderItem(
                    id=oi.id,
                    quantity=oi.quantity,
                    menuId=oi.item_id,
                    price=str(oi.price),  # Convert float to string as per schema
                    name=oi.item.name if oi.item else "Unknown Item",  # Get name from related item
                )
            )

    return Order(
        userId=db_order.user_id,
        userName=db_order.user_name,
        totalPrice=db_order.total_price,
        status=db_order.status,
        fulfillmentType=db_order.fulfillment_type.value,
        items=items,
        id=db_order.id,
        createdAt=db_order.created_at.isoformat() if db_order.created_at else None,
        updatedAt=db_order.updated_at.isoformat() if db_order.updated_at else None,
    )