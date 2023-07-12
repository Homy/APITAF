# base_resource.py

from jsonschema import validate, ValidationError

class BaseResource:
    def __init__(self, api_client, schema):
        self.api_client = api_client
        self.schema = schema

    def validate_resource_data(self, resource_data):
        try:
            validate(resource_data, self.schema)
        except ValidationError as e:
            raise AssertionError(f"Invalid resource data: {e.message}")

    def _get_json_response(self, response):
        resource_data = response.json()
        self.validate_resource_data(resource_data)
        return resource_data

    def get(self, resource_id):
        endpoint = f"{self.endpoint}/{resource_id}"
        response = self.api_client.send_request("GET", endpoint)
        return self._get_json_response(response)

    def create(self, resource_data):
        self.validate_resource_data(resource_data)

        response = self.api_client.send_request("POST", self.endpoint, resource_data)
        return self._get_json_response(response)

    def update(self, resource_id, resource_data):
        self.validate_resource_data(resource_data)

        endpoint = f"{self.endpoint}/{resource_id}"
        response = self.api_client.send_request("PUT", endpoint, resource_data)
        return self._get_json_response(response)

    def delete(self, resource_id):
        endpoint = f"{self.endpoint}/{resource_id}"
        response = self.api_client.send_request("DELETE", endpoint)
        return response.status_code
