from datetime import datetime, UTC
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.cart_item_model import CartItemModel
    from app.models.order_item import OrderItemModel


# Define category enumeration
class CategoryEnum(str, Enum):
    """Enumeration for dish categories"""
    MAIN_COURSES = "Main Courses"
    DESSERTS = "Desserts"
    BEVERAGES = "Beverages"


class ItemModel(SQLModel, table = True):
    """Database model for menu items"""
    __tablename__ = "item"
    id: Optional[int] = Field(default = None, primary_key = True, description = "Unique identifier for the menu item")
    name: str = Field(unique = True, index = True, max_length = 100, description = "Name of the dish")
    description: str = Field(default = "", max_length = 500, description = "Detailed description of the dish")
    price: float = Field(gt = 0, description = "Price of the dish as a floating-point number")
    category: CategoryEnum = Field(index = True,
                                   description = "Category of the dish (Main Courses, Desserts, Beverages)")
    imageUrl: str = Field(default = "", max_length = 500, description = "URL pointing to the dish image")
    available: bool = Field(default = False, description = "Availability status of the dish")
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory = lambda: datetime.now(UTC),
        sa_column_kwargs = {"onupdate": lambda: datetime.now(UTC)})

    cart_items: list["CartItemModel"] = Relationship(back_populates="item")
    # Link to order items for inventory updates via relationship
    order_items: list["OrderItemModel"] = Relationship(back_populates="item")
