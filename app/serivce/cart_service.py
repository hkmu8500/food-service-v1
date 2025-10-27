from app.models.cart_model import CartModel
from app.persistence.repositories.cart_repository import CartRepository
from app.core.db_config import get_db_session_sync


class CartService:
    """Contains business logic for cart operations."""

    def __init__(self, repository: CartRepository):
        self.repository = repository

    def create_cart(self, user_id: int) -> CartModel:
        existing_cart = self.repository.get_cart_by_user_id(user_id)
        if existing_cart:
            raise ValueError("User already has an existing cart")

        cart = CartModel(user_id=user_id)
        return self.repository.create_cart(cart)
    
    def get_user_cart(self, user_id: int) -> CartModel:
        print("Looking for cart for user:", user_id)
        cart = self.repository.get_cart_by_user_id(user_id)
        print("Found cart:", cart)
        if not cart:
            raise ValueError(f"Cart for user {user_id} not found")
        return cart


