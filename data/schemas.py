# schemas.py

import yaml

SCHEMA_FILE = "data/schemas.yaml"
SCHEMAS = {}

def load_schemas():
    with open(SCHEMA_FILE) as file:
        return yaml.safe_load(file)

def get_schema(schema_name):
    if not SCHEMAS:
        SCHEMAS.update(load_schemas())
    return SCHEMAS.get(schema_name, {})

USER_SCHEMA = get_schema("USER_SCHEMA")
POST_SCHEMA = get_schema("POST_SCHEMA")
