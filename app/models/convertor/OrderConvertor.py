from app.models.order_model import OrderModel, FulfillmentTypeEnum
from app.models.schemas.order import Order
from app.models.enums.order_status import OrderStatusEnum


def order_model_to_order(db_order: OrderModel) -> Order:
    """Convert SQLModel OrderModel to Pydantic Order"""
    return Order(
        id = db_order.id,
        user_id = db_order.user_id,
        item_id = db_order.item_id,
        quantity = db_order.quantity,
        total_price = db_order.total_price,
        status = db_order.status,
        fulfillment_type = db_order.fulfillment_type.name,
    )

def order_to_order_model(order: Order) -> OrderModel:
    """Convert Pydantic Order to SQLModel OrderModel"""
    return OrderModel(
        id = order.id,
        user_id = order.user_id,
        item_id = order.item_id,
        quantity = order.quantity,
        total_price = order.total_price,
        status = order.status,
        fulfillment_type = FulfillmentTypeEnum(order.fulfillment_type)
        # created_at and updated_at will be auto-generated
    )