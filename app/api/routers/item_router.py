from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db_config import get_db_session
from app.models.convertor.ItemConvertor import item_model_to_item
from app.models.schemas.Item import Item
from app.models.schemas.base_response import BaseResponse
from app.persistence.repositories.item_repository import ItemRepository
from app.serivce.item_service import ItemService

router = APIRouter(prefix = "/api")


def get_item_service(session: Session = Depends(get_db_session)) -> ItemService:
    """Dependency that provides ItemService instance"""
    repository = ItemRepository(session)
    return ItemService(repository)


@router.get("/menu", response_model = BaseResponse[list[Item]])
def get_menu(service: ItemService = Depends(get_item_service)) -> BaseResponse[list[Item]]:
    item_models = service.get_items_by_filters(category = None, available = None)

    if len(item_models) == 0:
        raise HTTPException(status_code = 404, detail = "No items found")

    items = list(map(item_model_to_item, item_models))

    return BaseResponse.create_success(data = items)
