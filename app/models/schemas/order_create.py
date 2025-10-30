from pydantic import BaseModel


class OrderCreateItem(BaseModel):
    item_id: int
    quantity: int


class OrderCreate(BaseModel):
    fulfillment_type: str
    items: list[OrderCreateItem]