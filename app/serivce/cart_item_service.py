from app.models.cart_item_model import CartItemModel
from app.persistence.repositories.cart_item_repository import CartItemRepository


class CartItemService:
    """Contains business logic for managing items within a user's cart."""

    def __init__(self, repository: CartItemRepository):
        self.repository = repository

    def add_item(self, cart_id: int, item_id: int, quantity: int) -> CartItemModel:
        if quantity <= 0:
            raise ValueError("Quantity Error")

        existing_item = self.repository.get_item_by_cart_and_item_id(cart_id, item_id)
        if existing_item:
            new_quantity = existing_item.quantity + quantity
            return self.repository.update_quantity(existing_item, new_quantity)

        new_cart_item = CartItemModel(cart_id=cart_id, item_id=item_id, quantity=quantity)
        return self.repository.add_item_to_cart(new_cart_item)

