from app.api.routers.item_router import get_item_service
from app.api.routers.order_router import get_order_service
from app.api.routers.user_router import get_user_service
from app.core.db_config import get_db_session_sync
from app.models.item_model import ItemModel, CategoryEnum
from app.models.order_model import OrderModel, FulfillmentTypeEnum


def init_db():
    print("Initializing DB")
    init_user()
    init_item()
    init_order()


def init_item():
    service = get_item_service(get_db_session_sync())
    service.create_item(ItemModel(name = "Bugger", description = "Bugger description", price = 100,
                                  category = CategoryEnum.MAIN_COURSES,
                                  imageUrl = "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg",
                                  available = True), )
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
    service.create_order(OrderModel(user_id = 1, item_id = 1, quantity = 2, total_price = 200,
                                    fulfillment_type = FulfillmentTypeEnum.DINE_IN))
