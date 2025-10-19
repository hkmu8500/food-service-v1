from app.api.routers.user_router import signup
from app.models.user import User 

def test_signup():
    
    response = signup("Kevin")

    assert response.message == "Success"
    assert isinstance(response.data, User)

    assert response.data.name == "Kevin"
    assert response.data.id == 1


if __name__ == "__main__":
    test_signup()
    print("Signup function: pass")