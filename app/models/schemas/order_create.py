from pydantic import BaseModel
from app.models.order_model import FulfillmentTypeEnum


class OrderCreateItem(BaseModel):
    menuId: int
    quantity: int


class OrderCreate(BaseModel):
    items: list[OrderCreateItem]


class OrderCreateCartItems(BaseModel):
    menuIds: list[int]
