from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db_config import get_db_session
from app.models.schemas.cart_item import Cart_Item
from app.models.schemas.base_response import BaseResponse
from app.persistence.repositories.cart_item_repository import CartItemRepository
from app.serivce.cart_item_service import CartItemService

router = APIRouter(prefix="/api/cart-items", tags=["Cart Items"])


def get_cart_item_service(session: Session = Depends(get_db_session)) -> CartItemService:
    """Dependency that provides CartItemService instance"""
    repository = CartItemRepository(session)
    return CartItemService(repository)


@router.post("/", response_model=BaseResponse[Cart_Item])
def add_item_to_cart(
    cart_id: int,
    item_id: int,
    quantity: int = 1,
    service: CartItemService = Depends(get_cart_item_service),
) -> BaseResponse[Cart_Item]:
    """Add an item to a user's cart"""
