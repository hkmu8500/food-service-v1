from datetime import datetime, UTC
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum


class OrderStatusEnum(str, Enum):
    """Enumeration for order status"""
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"

class FulfillmentTypeEnum(str, Enum):
    """Enumeration for fulfillment types"""
    DINE_IN = "dine-in"
    PICKUP = "pickup"
    DELIVERY = "delivery"

class OrderModel(SQLModel, table = True):
    """Database model for order"""
    __tablename__ = "orders"
    id: Optional[int] = Field(default = None, primary_key = True, description = "Unique identifier for the order")
    user_id: int = Field(description = "ID of the user who placed the order")
    user_name: str = Field(description = "Name of the user who placed the order")
    total_price: float = Field(gt = 0, description = "Total price of the order")
    status: OrderStatusEnum = Field(default = OrderStatusEnum.PENDING, description = "Status of the order")
    fulfillment_type: FulfillmentTypeEnum = Field(description = "Fulfillment type of the order")
   
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory = lambda: datetime.now(UTC),
        sa_column_kwargs = {"onupdate": lambda: datetime.now(UTC)})

    # Relationship to order items with cascade for inserts/deletes
    items: list["OrderItemModel"] = Relationship(
        back_populates = "order",
        sa_relationship_kwargs = {"cascade": "all, delete-orphan", "lazy": "selectin"}
    )
    