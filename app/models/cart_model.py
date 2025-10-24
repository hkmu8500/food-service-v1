from datetime import datetime, UTC
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:                                   
    from app.models.user_model import UserModel
    from app.models.cart_item_model import CartItemModel


class CartModel(SQLModel, table=True):
    """Database model for shopping cart (order cart)."""

    __tablename__ = "cart"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)},
    )

    user: Optional["UserModel"] = Relationship(back_populates="cart")
    items: list["CartItemModel"] = Relationship(back_populates="cart")
