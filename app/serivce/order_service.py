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

    def get_orders_by_filters(self, user_id: int) -> list[OrderModel]:
        """Get orders by filter"""
        return self.repository.get_orders_by_filter(user_id)
