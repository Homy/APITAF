from conftest import users

def test_get_user(users):
    user_id = 1
    user = users.get(user_id)
    assert isinstance(user, dict)
    assert user["id"] == user_id

def test_create_user(users):
    new_user = {
        "id": 101,
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com",
        "address": {
            "street": "123 Main Street",
            "suite": "Apt. 4",
            "city": "New York",
            "zipcode": "10001",
            "geo": {
                "lat": "40.7128",
                "lng": "-74.0060"
            }
        }
    }
    created_user = users.create(new_user)
    assert isinstance(created_user, dict)
    assert created_user["id"] is not None

def test_update_user(users):
    user_id = 1
    updated_user_data = {
        "id": user_id,
        "name": "Updated Name",
        "username": "updatedusername",
        "email": "updated.email@example.com",
        "address": {
            "street": "Updated Street",
            "suite": "Apt. 123",
            "city": "Updated City",
            "zipcode": "12345",
            "geo": {
                "lat": "12.3456",
                "lng": "34.5678"
            }
        }
    }
    updated_user = users.update(user_id, updated_user_data)
    assert isinstance(updated_user, dict)
    assert updated_user["name"] == "Updated Name"

def test_delete_user(users):
    user_id = 1
    delete_status = users.delete(user_id)
    assert delete_status == 200
