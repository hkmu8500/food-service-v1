from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db_config import get_db_session
from app.models.convertor.UserConvertor import user_model_to_user
from app.models.schemas.base_response import BaseResponse
from app.models.schemas.user import User
from app.persistence.repositories.user_repository import UserRepository
from app.serivce.user_service import UserService

router = APIRouter(prefix = "/api")


def get_user_service(session: Session = Depends(get_db_session)) -> UserService:
    """Dependency that provides UserService instance"""
    repository = UserRepository(session)
    return UserService(repository)


@router.post("/auth/signup", response_model = BaseResponse[User])
def signup(user_name: str, service: UserService = Depends(get_user_service)) -> BaseResponse[User]:
    user_model = service.signup(user_name)
    user = user_model_to_user(user_model)
    return BaseResponse.create_success(data = user)


@router.post("/auth/login", response_model = BaseResponse[User])
def login(user_name: str, service: UserService = Depends(get_user_service)) -> BaseResponse[User]:
    user_model = service.login(user_name)
    user = user_model_to_user(user_model)
    return BaseResponse.create_success(data = user)
