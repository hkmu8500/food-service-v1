from app.api.routers.item_router import get_item_service
from app.api.routers.user_router import get_user_service
from app.core.db_config import get_db_session_sync
from app.models.item_model import ItemModel, CategoryEnum


def init_db():
    print("Initializing DB")
    init_user()
    init_item()


def init_item():
    service = get_item_service(get_db_session_sync())
    service.create_item(ItemModel(name = "Bugger", description = "Bugger description", price = 100,
                                  category = CategoryEnum.MAIN_COURSES,
                                  image_url = "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg",
                                  available = True))
    service.create_item(ItemModel(name = "Milk Tea", description = "Milk Tea description", price = 50,
                                  category = CategoryEnum.BEVERAGES,
                                  image_url = "https://images.pexels.com/photos/4974543/pexels-photo-4974543.jpeg",
                                  available = True))


def init_user():
    service = get_user_service(get_db_session_sync())
    service.signup(name = "hkmu")
    service.signup(name = "8500")
