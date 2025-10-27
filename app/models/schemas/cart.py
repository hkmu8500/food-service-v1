from pydantic import BaseModel
from typing import List

from app.models.schemas.user import User
from app.models.schemas.cart_item import Cart_Item


class Cart(BaseModel):
    """
    A Pydantic model representing the order cart. 
    """
    id: int
    user: User
    items: List[Cart_Item] = []

    
   