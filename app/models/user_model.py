from datetime import datetime, UTC
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:                                
    from app.models.cart_model import CartModel


class UserModel(SQLModel, table = True):
    """Database model for user"""

    __tablename__ = "user"

    id: Optional[int] = Field(default = None, primary_key = True, description = "Unique identifier for the user")
    name: str = Field(unique = True, index = True, max_length = 100, description = "Name of the user")
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = Field(
        default_factory = lambda: datetime.now(UTC),
        sa_column_kwargs = {"onupdate": lambda: datetime.now(UTC)})
    
    cart: Optional["CartModel"] = Relationship(back_populates="user")
