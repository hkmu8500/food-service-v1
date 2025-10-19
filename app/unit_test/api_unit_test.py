import requests

def test_signup_success():
    url = "http://localhost:5001/api/auth/signup"
    params = {"user_name": "Kevin"}

    response = requests.post(url, params=params)

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Success"
    assert isinstance(data["data"]["id"], int) and data["data"]["id"] > 0 #Checks if the id is a higher number then 0

if __name__ == "__main__":
    test_signup_success()
    print("Sign up unit test passed")