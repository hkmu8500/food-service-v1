from app.models.cart_item_model import CartItemModel
from app.models.schemas.cart_item import Cart_Item
from app.models.convertor.ItemConvertor import item_model_to_item, item_to_item_model


def cart_item_model_to_cart_item(db_cart_item: CartItemModel) -> Cart_Item:
    """Convert SQLModel CartItemModel to Pydantic Cart_Item"""
    return Cart_Item(
        id=db_cart_item.id,
        quantity=db_cart_item.quantity,
        items=item_model_to_item(db_cart_item.item)  
    )


def cart_item_to_cart_item_model(cart_item: Cart_Item) -> CartItemModel:
    """Convert Pydantic Cart_Item to SQLModel CartItemModel"""
    return CartItemModel(
        id=cart_item.id,
        quantity=cart_item.quantity,
        item=item_to_item_model(cart_item.items)  
    )
