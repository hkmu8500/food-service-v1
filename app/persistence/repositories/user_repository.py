from sqlmodel import Session, select

from app.models.user_model import UserModel


class UserRepository:
    # Handles all database operations for users

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_data: UserModel) -> UserModel:
        # Create a new user in database
        self.session.add(user_data)
        self.session.commit()
        self.session.refresh(user_data)
        return user_data

    def get_user_by_name(self, name: str) -> UserModel | None:
        # Get user by name
        if name is None:
            return None
        statement = select(UserModel).where(UserModel.name == name)
        return self.session.exec(statement).first()

    def update_user(self, user_id: int, user_data: UserModel) -> UserModel | None:
        # Update user information
        db_user: UserModel | None = self.session.get(UserModel, user_id)
        if not db_user:
            return None

        update_data = user_data.model_dump(exclude_unset = True)

        for field, value in update_data.items():
            setattr(db_user, field, value)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user
