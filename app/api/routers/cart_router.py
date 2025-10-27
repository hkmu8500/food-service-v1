from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.db_config import get_db_session
from app.models.convertor.CartConvertor import cart_model_to_cart
from app.models.schemas.cart import Cart
from app.models.schemas.base_response import BaseResponse
from app.persistence.repositories.cart_repository import CartRepository
from app.serivce.cart_service import CartService

router = APIRouter(prefix="/api", tags=["Cart"])

def get_cart_service(session: Session = Depends(get_db_session)) -> CartService:
    """Dependency that provides CartService instance"""
    repository = CartRepository(session)
    return CartService(repository)

# Saves a cart for a user
@router.post("/cart/{user_id}", response_model=BaseResponse[Cart])
def create_cart(user_id: int, service: CartService = Depends(get_cart_service)) -> BaseResponse[Cart]:
    """Create a new cart for a given user"""
    cart_model = service.create_cart(user_id)
    cart = cart_model_to_cart(cart_model)
    return BaseResponse.create_success(data=cart)

# Searches a cart for a user 
@router.get("/cart/{user_id}", response_model=BaseResponse[Cart])
def get_user_cart(user_id: int, service: CartService = Depends(get_cart_service)) -> BaseResponse[Cart]:

    cart_model = service.get_user_cart(user_id)
    cart = cart_model_to_cart(cart_model)
    return BaseResponse.create_success(data=cart)

