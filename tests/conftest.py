import pytest
import yaml
from clients.api_client import APIClient
from clients.users import Users
from clients.posts import Posts


def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


config = load_config()
BASE_URL = config["base_url"]


@pytest.fixture(scope="module")
def api_client():
    return APIClient(BASE_URL)


@pytest.fixture(scope="module")
def users(api_client):
    return Users(api_client)


@pytest.fixture(scope="module")
def posts(api_client):
    return Posts(api_client)
