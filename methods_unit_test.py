from unittest.mock import MagicMock, PropertyMock
from app.api.routers.user_router import signup, login
from app.models.schemas.user import User
from app.models.schemas.base_response import BaseResponse

def signup_method_test(service, username, expected_id, expected_name):
    response = signup(username, service=service)
    
    assert isinstance(response, BaseResponse)
    assert response.message == "Success"
    assert isinstance(response.data, User)
    assert response.data.name == expected_name
    assert response.data.id == expected_id

def login_method_test(service, username, expected_id, expected_name):
    response = login(username, service=service)
    
    assert isinstance(response, BaseResponse)
    assert response.message == "Success"
    assert isinstance(response.data, User)
    assert response.data.name == expected_name
    assert response.data.id == expected_id

if __name__ == "__main__":
    # Test 1
    mock_user_model1 = MagicMock()
    mock_user_model1.id = 1
    type(mock_user_model1).name = PropertyMock(return_value="Kevin")

    mock_service1 = MagicMock()
    mock_service1.signup.return_value = mock_user_model1
    mock_service1.login.return_value = mock_user_model1

    # Test 2
    mock_user_model2 = MagicMock()
    mock_user_model2.id = 2
    type(mock_user_model2).name = PropertyMock(return_value="Patrick")

    mock_service2 = MagicMock()
    mock_service2.signup.return_value = mock_user_model2
    mock_service2.login.return_value = mock_user_model2  

    # Signup test
    signup_method_test(mock_service1, username="Kevin", expected_id=1, expected_name="Kevin")
    signup_method_test(mock_service2, username="Patrick", expected_id=2, expected_name="Patrick")
    print("Sign-up method pass (2 test cases)")

    # Login test
    login_method_test(mock_service1, username="Kevin", expected_id=1, expected_name="Kevin")
    login_method_test(mock_service2, username="Patrick", expected_id=2, expected_name="Patrick")
    print("Login method pass (2 test cases)")