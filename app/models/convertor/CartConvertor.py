from typing import List

from app.models.cart_model import CartModel
from app.models.cart_item_model import CartItemModel
from app.models.schemas.cart import Cart
from app.models.schemas.cart_item import Cart_Item

from app.models.convertor.UserConvertor import user_model_to_user
from app.models.convertor.UserConvertor import user_to_user_model
from app.models.convertor.CartItemConvertor import cart_item_model_to_cart_item
from app.models.convertor.CartItemConvertor import cart_item_to_cart_item_model



def cart_model_to_cart(db_cart: CartModel) -> Cart:
    """Convert SQLModel CartModel to Pydantic Cart"""
    
    user = user_model_to_user(db_cart.user) if db_cart.user else None
    
    items: List[Cart_Item] = []
    if db_cart.items:
        items = [cart_item_model_to_cart_item(ci) for ci in db_cart.items]
    
    return Cart(
        id=db_cart.id,
        user=user,
        items=items
    )


def cart_to_cart_model(cart: Cart) -> CartModel:
    """Convert Pydantic Cart to SQLModel CartModel"""
    
    user_model = user_to_user_model(cart.user) if cart.user else None
    

    cart_items_models: List[CartItemModel] = []
    if cart.items:
        cart_items_models = [cart_item_to_cart_item_model(ci) for ci in cart.items]
    
    return CartModel(
        id=cart.id,
        user=user_model,
        items=cart_items_models
    )
