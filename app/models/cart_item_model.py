from datetime import datetime, UTC
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.cart_model import CartModel
    from app.models.item_model import ItemModel


class CartItemModel(SQLModel, table=True):
    """Database model for an item within a user's order cart."""

    __tablename__ = "cart_item"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    cart_id: int = Field(
        foreign_key="cart.id",
        index=True
    )
    item_id: int = Field(
        foreign_key="item.id",
        index=True
    )
    quantity: int = Field(default=0)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)},
    )

    cart: Optional["CartModel"] = Relationship(back_populates="items")
    item: Optional["ItemModel"] = Relationship(back_populates="cart_items")