from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: str
    category: str
    imageUrl: str
    available: bool


class CartItemResponse(BaseModel):
    id: int
    quantity: int
    items: ItemResponse  
