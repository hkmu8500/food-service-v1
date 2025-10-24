from pydantic import BaseModel
from app.models.schemas.Item import Item  # Make sure the Item model exists

class Cart_Item(BaseModel):
    """
    A Pydantic model representing the order cart item.
    """
    id: int
    quantity: int
    items: Item
