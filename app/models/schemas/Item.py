from pydantic import BaseModel


class Item(BaseModel):
    """
    A Pydantic model representing a dish item on a menu.
    This model validates the structure of dish data, ensuring it has a name and price.
    """
    # The name of the dish (e.g., "Margherita Pizza")
    id: int
    name: str
    description: str
    # The price of the dish, represented as a str
    price: str
    # category（E.g. Main Courses, Desserts, Beverages）
    category: str
    imageUrl: str
    available: bool = False
