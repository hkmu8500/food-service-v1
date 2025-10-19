from app.models.item_model import ItemModel, CategoryEnum
from app.persistence.repositories.item_repository import ItemRepository


class ItemService:
    """Contains business logic for item operations"""

    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def create_item(self, item_model: ItemModel) -> ItemModel:
        if item_model is None or item_model.name is None:
            raise ValueError("Item name is required")

        # Check if name already exists
        if self.repository.get_item_by_name(item_model.name):
            raise ValueError("name already existed")

        # Create item in database
        db_user = self.repository.create_item(item_model)
        return db_user

    def get_items_by_filters(self, category: CategoryEnum | None,
                             available: bool | None) -> list[ItemModel]:
        return self.repository.get_items_by_filters(category, available)
