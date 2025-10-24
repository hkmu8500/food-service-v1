from app.api.routers.item_router import get_item_service
from app.api.routers.user_router import get_user_service
from app.core.db_config import get_db_session_sync
from app.models.item_model import ItemModel, CategoryEnum
from app.models.order_model import OrderModel
from app.api.routers.order_router import get_order_service        
from app.models.cart_model import CartModel          
from app.models.cart_item_model import CartItemModel 
from app.api.routers.cart_router import get_cart_service
from app.api.routers.cart_item_router import get_cart_item_service
from sqlmodel import select


def init_db():
    print("Initializing DB")

    init_user()
    init_item()
    init_order()
    init_cart()
    init_cart_item()

    session = get_db_session_sync()

    # Checking part
    carts = session.exec(select(CartModel)).all()
    print("Carts in DB after init:", carts)
    items = session.exec(select(ItemModel)).all()
    print("Items in DB after init:", items)


def init_item():
    service = get_item_service(get_db_session_sync())
    service.create_item(ItemModel(name = "Bugger", description = "Bugger description", price = 100,
                                  category = CategoryEnum.MAIN_COURSES,
                                  imageUrl = "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg",
                                  available = True),)
    service.create_item(ItemModel(name = "Milk Tea", description = "Milk Tea description", price = 50,
                                  category = CategoryEnum.BEVERAGES,
                                  imageUrl = "https://images.pexels.com/photos/4974543/pexels-photo-4974543.jpeg",
                                  available = True))


def init_user():
    service = get_user_service(get_db_session_sync())
    service.signup(name = "hkmu")
    service.signup(name = "8500")
    service.signup(name = "test")
    service.signup(name = "admin")


def init_order():
    service = get_order_service(get_db_session_sync())
    service.create_order(OrderModel(user_id = 1, item_id = 1, quantity = 2, total_price = 200))


def init_cart():
    service = get_cart_service(get_db_session_sync())
    service.create_cart(user_id=1)
    service.create_cart(user_id=2)


def init_cart_item():
    service = get_cart_item_service(get_db_session_sync())
    service.add_item(cart_id=1, item_id=1, quantity=2)
    service.add_item(cart_id=1, item_id=2, quantity=1)
    service.add_item(cart_id=2, item_id=1, quantity=3)

