from pydantic import BaseModel

from app.models.schemas.Item import Item

class OrderItem(BaseModel):
    """
    A Pydantic model representing the order item.
    """
    id: int
    quantity: int
    item: Item
    price: float
