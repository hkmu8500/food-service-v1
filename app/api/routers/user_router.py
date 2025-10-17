from fastapi import APIRouter

from app.core.schemas import BaseResponse
from app.models.Item import Item
from app.models.user import User

router = APIRouter(prefix = "/api")


@router.post("/auth/signup", response_model = BaseResponse[User])
def signup(user_name: str) -> BaseResponse[User]:

    user = User(id = 1, name = user_name)
    return BaseResponse.create_success(data = user)

@router.post("/auth/login", response_model = BaseResponse[User])
def login(user_name: str) -> BaseResponse[User]:

    user = User(id = 1, name = user_name)
    return BaseResponse.create_success(data = user)
