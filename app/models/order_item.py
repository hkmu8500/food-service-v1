from datetime import datetime, UTC
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.order_model import OrderModel
    from app.models.item_model import ItemModel


class OrderItemModel(SQLModel, table=True):
    __tablename__ = "order_item"

    id: Optional[int] = Field(default=None, primary_key=True, description="Unique identifier for the order item")
    quantity: int = Field(gt=0, description="Quantity of the item ordered")

    item_id: int = Field(foreign_key="item.id", index=True, description="ID of the item ordered")
    price: float = Field(gt=0, description="Price of the item")
    total_price: float = Field(gt=0, description="Total price of the item (quantity * price)")
    order_id: int = Field(foreign_key="orders.id", index=True, description="ID of the order this item belongs to")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)},
    )

    # Relationships
    order: Optional["OrderModel"] = Relationship(back_populates="items")
    item: Optional["ItemModel"] = Relationship(back_populates="order_items")