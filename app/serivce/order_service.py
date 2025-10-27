from app.models.order_model import OrderModel
from app.persistence.repositories.order_repository import OrderRepository

class OrderService():
    """Service for OrderModel"""
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order: OrderModel) -> OrderModel:
        """Create a new order"""
        return self.repository.create_order(order)

    def get_orders(self) -> list[OrderModel]:
        """Get all orders"""
        return self.repository.get_orders()