from pydantic import BaseModel
from app.models.order_model import OrderStatusEnum, FulfillmentTypeEnum


class Order(BaseModel):
    '''
    A Pydantic model representing an order placed by a user.
    This model validates the structure of order data, ensuring it has a user ID, item ID, quantity, and total price.
    '''
    user_id: int
    item_id: int
    quantity: int
    total_price: float
    status: OrderStatusEnum = OrderStatusEnum.PENDING
    fulfillment_type: str