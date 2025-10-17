from fastapi import APIRouter

from app.core.schemas import BaseResponse
from app.models.Item import Item

router = APIRouter(prefix = "/api")


@router.get("/menu", response_model = BaseResponse[list[Item]])
def get_menu() -> BaseResponse[list[Item]]:
    items = [Item(id = 1, name = "dish", price = "1.00", category = "dish", imageUrl = "", available = True)]
    return BaseResponse.create_success(data = items)
