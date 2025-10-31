from pydantic import BaseModel
from app.models.order_model import OrderStatusEnum, FulfillmentTypeEnum
from app.models.schemas.order_item import OrderItem


class Order(BaseModel):
    '''
    A Pydantic model representing an order placed by a user.
    This model validates the structure of order data, ensuring it has a user ID, item ID, quantity, and total price.
    '''
    user_id: int
    total_price: float
    status: OrderStatusEnum = OrderStatusEnum.PENDING
    fulfillment_type: str
    items: list[OrderItem] = []

# Ensure forward references (if any) are resolved in Pydantic v2
try:
    Order.model_rebuild()
except Exception:
    # Safe no-op if rebuild is unnecessary or already done
    pass
