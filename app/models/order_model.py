from datetime import datetime, UTC
from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum


class OrderStatusEnum(str, Enum):
    """Enumeration for order status"""
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"

class OrderModel(SQLModel, table = True):
    """Database model for order"""
    __tablename__ = "order"
    id: Optional[int] = Field(default = None, primary_key = True, description = "Unique identifier for the order")
    user_id: int = Field(description = "ID of the user who placed the order")
    item_id: int = Field(description = "ID of the item ordered")
    quantity: int = Field(gt = 0, description = "Quantity of the item ordered")
    total_price: float = Field(gt = 0, description = "Total price of the order")
    status: OrderStatusEnum = Field(default = OrderStatusEnum.PENDING, description = "Status of the order")
   
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory = lambda: datetime.now(UTC),
        sa_column_kwargs = {"onupdate": lambda: datetime.now(UTC)})