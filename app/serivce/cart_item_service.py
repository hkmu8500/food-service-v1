from app.models.cart_item_model import CartItemModel
from app.persistence.repositories.cart_item_repository import CartItemRepository
from app.persistence.repositories.cart_repository import CartRepository
from app.models.schemas.cart_item_response import CartItemResponse, ItemResponse



class CartItemService:
    """Contains business logic for managing items within a user's cart."""

    def __init__(self, cart_repository: CartRepository, cart_item_repository: CartItemRepository):
        self.cart_repository = cart_repository
        self.cart_item_repository = cart_item_repository

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
        existing_item = self.cart_item_repository.get_item_by_cart_and_item_id(cart_id, item_id)
        if existing_item:
            existing_item.quantity += 1
            updated_item = self.cart_item_repository.update(existing_item)
            return self.map_cart_item(updated_item) 
        else:
            new_item = CartItemModel(cart_id=cart_id, item_id=item_id, quantity=1)
            created_item = self.cart_item_repository.create(new_item)
            return self.map_cart_item(created_item)  
    
    
    def add_item_by_user_id(self, user_id: int, item_id: int) -> CartItemResponse:
        cart = self.cart_repository.get_cart_by_user_id(user_id)   
        
        existing_item = self.cart_item_repository.get_item_by_cart_and_item_id(cart.id, item_id)
        if not cart:
            cart = self.cart_repository.create_cart(user_id)
        return self.add_item(cart.id, item_id)

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

