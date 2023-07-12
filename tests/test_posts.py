# test_posts.py

import pytest
from clients.api_client import APIClient
from clients.posts import Posts

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture(scope="module")
def posts(api_client):
    return Posts(api_client)

def test_get_post(posts):
    post_id = 1
    post = posts.get(post_id)
    assert isinstance(post, dict)
    assert post["id"] == post_id

def test_create_post(posts):
    new_post = {
        "userId": 1,
        "id": 101,
        "title": "New Post Title",
        "body": "New post body"
    }
    created_post = posts.create(new_post)
    assert isinstance(created_post, dict)
    assert created_post["id"] is not None

def test_update_post(posts):
    post_id = 1
    updated_post_data = {
        "userId": 1,
        "id": post_id,
        "title": "Updated Post Title",
        "body": "Updated post body"
    }
    updated_post = posts.update(post_id, updated_post_data)
    assert isinstance(updated_post, dict)
    assert updated_post["title"] == "Updated Post Title"

def test_delete_post(posts):
    post_id = 1
    delete_status = posts.delete(post_id)
    assert delete_status == 200
