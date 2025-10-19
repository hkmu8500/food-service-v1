from sqlmodel import Session, select

from app.models.item_model import ItemModel, CategoryEnum


class ItemRepository:
    # Handles all database operations for items

    def __init__(self, session: Session):
        self.session = session

    def create_item(self, item_data: ItemModel) -> ItemModel:
        # Create a new item in database
        self.session.add(item_data)
        self.session.commit()
        self.session.refresh(item_data)
        return item_data

    def get_items_by_filters(self, category: CategoryEnum | None,
                             available: bool | None) -> list[ItemModel]:
        # Get items by filters
        statement = select(ItemModel)

        if category is not None:
            statement = statement.where(ItemModel.category == category.name)
        if available is not None:
            statement = statement.where(ItemModel.available == available)

        results = self.session.exec(statement)
        return list(results.all())

    def get_item_by_name(self, name: str) -> ItemModel | None:
        # Get item by name
        if name is None:
            return None
        statement = select(ItemModel).where(ItemModel.name == name)
        return self.session.exec(statement).first()

