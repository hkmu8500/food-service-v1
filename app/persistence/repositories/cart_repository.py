from sqlmodel import Session, select
from typing import Optional, List

from app.models.cart_model import CartModel


class CartRepository:
    """Handles persistence operations for carts."""

    def __init__(self, session: Session):
        self.session = session

    def create_cart(self, cart: CartModel) -> CartModel:
        self.session.add(cart)
        self.session.commit()
        self.session.refresh(cart)
        return cart

    def get_cart_by_user_id(self, user_id: int) -> Optional[CartModel]:
        statement = select(CartModel).where(CartModel.user_id == user_id)
        return self.session.exec(statement).first()

    def delete_cart(self, cart_id: int) -> bool:
        cart = self.session.get(CartModel, cart_id)
        if not cart:
            return False
        self.session.delete(cart)
        self.session.commit()
        return True
    
    def get_cart_by_user_id(self, user_id: int) -> Optional[CartModel]:
        statement = select(CartModel).where(CartModel.user_id == user_id)
        return self.session.exec(statement).first()
