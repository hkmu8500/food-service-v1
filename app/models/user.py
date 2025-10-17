from pydantic import BaseModel


class User(BaseModel):
    """
    A Pydantic model representing a dish item on a menu.
    This model validates the structure of dish data, ensuring it has a name and price.
    """
    # The name of the dish (e.g., "Margherita Pizza")
    id: int
    name: str
