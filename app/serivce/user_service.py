from app.models.user_model import UserModel
from app.persistence.repositories.user_repository import UserRepository


class UserService:
    """Contains business logic for user operations"""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def signup(self, name: str) -> UserModel:
        """Register a new user with validation"""
        # Check if name already exists
        if self.repository.get_user_by_name(name):
            raise ValueError("name already registered")

        # Create user in database
        db_user = self.repository.create_user(UserModel(name = name))
        return db_user

    def login(self, name: str) -> UserModel | None:
        """Get user profile by ID"""
        db_user = self.repository.get_user_by_name(name)
        return db_user
