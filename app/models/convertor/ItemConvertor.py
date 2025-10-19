from app.models.item_model import ItemModel, CategoryEnum
from app.models.schemas.Item import Item


def item_model_to_item(db_item: ItemModel) -> Item:
    """Convert SQLModel ItemModel to Pydantic Item"""
    return Item(
        id = db_item.id,
        name = db_item.name,
        description = db_item.description,
        price = f"{db_item.price:.2f}",  # Convert float to string with 2 decimal places
        category = db_item.category.value,  # Get enum string value
        imageUrl = db_item.imageUrl,
        available = db_item.available
    )


def item_to_item_model(item: Item) -> ItemModel:
    """Convert Pydantic Item to SQLModel ItemModel"""
    return ItemModel(
        id = item.id,
        name = item.name,
        description = item.description,
        price = float(item.price),  # Convert string to float
        category = CategoryEnum(item.category),  # Convert string to enum
        imageUrl = item.imageUrl,
        available = item.available
        # created_at and updated_at will be auto-generated
    )
