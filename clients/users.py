# users.py

from .base_resource import BaseResource
from data.schemas import get_schema

class Users(BaseResource):
    def __init__(self, api_client):
        schema = get_schema("USER_SCHEMA")
        super().__init__(api_client, schema)
        self.endpoint = "users"
