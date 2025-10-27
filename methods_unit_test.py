from unittest.mock import MagicMock, PropertyMock
from app.api.routers.user_router import signup, login
from app.models.schemas.user import User
from app.models.schemas.base_response import BaseResponse

#Sign-up and Login Tests
def signup_method_test(service, username, expected_name):
    response = signup(username, service=service)
    
    assert isinstance(response, BaseResponse)
    assert response.message == "Success"
    assert isinstance(response.data, User)
    assert response.data.name == expected_name

def login_method_test(service, username, expected_name):
    response = login(username, service=service)
    
    assert isinstance(response, BaseResponse)
    assert response.message == "Success"
    assert isinstance(response.data, User)
    assert response.data.name == expected_name

if __name__ == "__main__":
    # Test 1
    mock_user_model1 = MagicMock()
    type(mock_user_model1).name = PropertyMock(return_value="Kevin")

    mock_service1 = MagicMock()
    mock_service1.signup.return_value = mock_user_model1
    mock_service1.login.return_value = mock_user_model1

    # Test 2
    mock_user_model2 = MagicMock()
    type(mock_user_model2).name = PropertyMock(return_value="Patrick")

    mock_service2 = MagicMock()
    mock_service2.signup.return_value = mock_user_model2
    mock_service2.login.return_value = mock_user_model2  

    # Signup test
    signup_method_test(mock_service1, username="Kevin", expected_name="Kevin")
    signup_method_test(mock_service2, username="Patrick", expected_name="Patrick")
    print("Sign-up method pass (2 test cases)")

    # Login test
    login_method_test(mock_service1, username="Kevin", expected_name="Kevin")
    login_method_test(mock_service2, username="Patrick", expected_name="Patrick")
    print("Login method pass (2 test cases)")

#Item tests