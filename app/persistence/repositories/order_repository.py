from sqlmodel import Session
from app.models.order_model import OrderModel

class OrderRepository():
    """Repository for OrderModel"""
    def __init__(self, session: Session):
        self.session = session

    def create_order(self, order: OrderModel) -> OrderModel:
        """Create a new order"""
        self.session.add(order)
        self.session.commit()
        self.session.refresh(order)
        return order

    def get_orders(self) -> list[OrderModel]:
        """Get all orders"""
        orders = self.session.query(OrderModel).all()
        return orders
    
    def get_order(self, order_id: int) -> OrderModel:
        """Get order by id"""
        order = self.session.query(OrderModel).filter(OrderModel.id == order_id).first()
        return order
        
    def update_order(self, order: OrderModel) -> OrderModel:
        """Update order"""
        self.session.add(order)
        self.session.commit()
        self.session.refresh(order)
        return order