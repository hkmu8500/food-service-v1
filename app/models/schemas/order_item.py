from pydantic import BaseModel

from app.models.schemas.Item import Item

class OrderItem(BaseModel):
    """
    A Pydantic model representing the order item.
    """
    id: int
    quantity: int
    # ID of the item in the menu
    menuId: int
    price: str
    name: str
