from app.models.schemas.user import User
from app.models.user_model import UserModel


def user_model_to_user(db_user: UserModel) -> User:
    """Convert SQLModel ItemModel to Pydantic Item"""
    return User(
        id = db_user.id,
        name = db_user.name,
    )


def user_to_user_model(user: User) -> UserModel:
    """Convert Pydantic Item to SQLModel ItemModel"""
    return UserModel(
        id = user.id,
        name = user.name,
        # created_at and updated_at will be auto-generated
    )
