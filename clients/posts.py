# posts.py

from .base_resource import BaseResource
from data.schemas import get_schema


class Posts(BaseResource):
    def __init__(self, api_client):
        schema = get_schema("POST_SCHEMA")
        super().__init__(api_client, schema)
        self.endpoint = "posts"
