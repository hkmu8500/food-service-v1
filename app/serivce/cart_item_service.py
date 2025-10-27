from app.models.cart_item_model import CartItemModel
from app.persistence.repositories.cart_item_repository import CartItemRepository
from app.models.schemas.cart_item_response import CartItemResponse, ItemResponse


class CartItemService:
    """Contains business logic for managing items within a user's cart."""

    def __init__(self, repository: CartItemRepository):
        self.repository = repository

    def map_cart_item(self, cart_item_model: CartItemModel) -> CartItemResponse:
        return CartItemResponse(
            id=cart_item_model.id,
            quantity=cart_item_model.quantity,
         items=ItemResponse(        
                id=cart_item_model.item.id,
                name=cart_item_model.item.name,
                description=cart_item_model.item.description,
                price=str(cart_item_model.item.price),  
                category=cart_item_model.item.category,
                imageUrl=cart_item_model.item.imageUrl,
                available=cart_item_model.item.available
        )
    )
    
    def add_item(self, cart_id: int, item_id: int) -> CartItemResponse:
        existing_item = self.repository.get_item_by_cart_and_item_id(cart_id, item_id)
        if existing_item:
            existing_item.quantity += 1
            updated_item = self.repository.update(existing_item)
            return self.map_cart_item(updated_item) 
        else:
            new_item = CartItemModel(cart_id=cart_id, item_id=item_id, quantity=1)
            created_item = self.repository.create(new_item)
            return self.map_cart_item(created_item)  

    # def add_item(self, cart_id: int, item_id: int) -> CartItemModel:
     
    #     print('Entered_02')
    #     existing_item = self.repository.get_item_by_cart_and_item_id(cart_id, item_id)

    #     if existing_item:
    #         print('Entered_03')
    #         existing_item.quantity += 1
    #         return self.repository.update(existing_item)
    #     else: 
    #         print('Entered_04')
    #         new_item = CartItemModel(cart_id=cart_id, item_id=item_id, quantity=1)
    #         return self.repository.create(new_item)

