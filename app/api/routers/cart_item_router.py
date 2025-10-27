from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.db_config import get_db_session
from app.models.schemas.cart_item import Cart_Item
from app.models.schemas.base_response import BaseResponse
from app.persistence.repositories.cart_item_repository import CartItemRepository
from app.serivce.cart_item_service import CartItemService
from app.models.schemas.cart_item_response import CartItemResponse

router = APIRouter(prefix="/api", tags=["Cart Items"])


def get_cart_item_service(session: Session = Depends(get_db_session)) -> CartItemService:
    """Dependency that provides CartItemService instance"""
    repository = CartItemRepository(session)
    return CartItemService(repository)

# Adds a cart item to the cart by 1
@router.post("/cart_item/{cart_id}/{item_id}", response_model=BaseResponse[CartItemResponse])
def add_item_to_cart(
    cart_id: int,
    item_id: int,

    service: CartItemService = Depends(get_cart_item_service),
) -> BaseResponse[CartItemResponse]:
    print('Entered_01')
    """Add an item to a user's cart"""
    try:
        cart_item = service.add_item(cart_id, item_id)
        print('Entered Try area')
        return BaseResponse.create_success(data=cart_item)
    
    except HTTPException as e:
        raise e