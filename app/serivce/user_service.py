from app.models.user_model import UserModel
from app.models.cart_model import CartModel
from app.persistence.repositories.user_repository import UserRepository
from app.persistence.repositories.cart_repository import CartRepository


class UserService:
    """Contains business logic for user operations"""

    def __init__(self, user_repository: UserRepository, cart_repository: CartRepository):
        self.user_repository = user_repository
        self.cart_repository = cart_repository

    def signup(self, name: str) -> UserModel:
        """Register a new user with validation"""
        # Check if name already exists
        if self.user_repository.get_user_by_name(name):
            raise ValueError("name already registered")

        # Create user in database
        db_user = self.user_repository.create_user(UserModel(name = name))

        cart_model = CartModel(user_id=db_user.id)
        self.cart_repository.create_cart(cart_model) 

        return db_user

    def login(self, name: str) -> UserModel | None:
        """Get user profile by ID"""
        db_user = self.user_repository.get_user_by_name(name)
        return db_user

    def get_user(self, user_id: int) -> UserModel | None:
        """Get user profile by ID"""
        db_user = self.user_repository.get_user(user_id)
        return db_user

    
