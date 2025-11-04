from sqlmodel import Session, select
from typing import Optional, List

from app.models.cart_item_model import CartItemModel


class CartItemRepository:
    """Handles persistence operations for CartItemModel."""

    def __init__(self, session: Session):
        self.session = session

    def create(self, cart_item: CartItemModel):
        self.session.add(cart_item)
        self.session.commit()
        self.session.refresh(cart_item)
        return cart_item

    def update(self, cart_item: CartItemModel):
        self.session.add(cart_item)
        self.session.commit()
        self.session.refresh(cart_item)
        return cart_item
    
    def add_item_to_cart(self, cart_item: CartItemModel) -> CartItemModel:
        self.session.add(cart_item)
        self.session.commit()
        self.session.refresh(cart_item)
        return cart_item

    def get_item(self, cart_item_id: int) -> Optional[CartItemModel]:
        return self.session.get(CartItemModel, cart_item_id)

    def get_items_by_cart_id(self, cart_id: int) -> List[CartItemModel]:
        statement = select(CartItemModel).where(CartItemModel.cart_id == cart_id)
        return list(self.session.exec(statement).all())

    def get_item_by_cart_and_item_id(
        self, cart_id: int, item_id: int
    ) -> Optional[CartItemModel]:
        statement = select(CartItemModel).where(
            (CartItemModel.cart_id == cart_id)
            & (CartItemModel.item_id == item_id)
        )
        return self.session.exec(statement).first()
    
    def delete_item(self, cart_item: CartItemModel) -> None:
        self.session.delete(cart_item)
        self.session.commit()

    def update_item_quantity(self, cart_id: int, item_id: int, quantity: int):
        cart_item = self.get_item_by_cart_and_item_id(cart_id, item_id)
        if not cart_item:
          return None  
    
        cart_item.quantity = quantity
        self.session.add(cart_item)
        self.session.commit()
        self.session.refresh(cart_item)
        return cart_item