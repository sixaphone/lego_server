connection_schema = {
    "type": "object",
    "required": ["name", "host", "auth_type", "password"],
    "properties": {
        "name": {"type": "string"},
        "host": {"type": "string"},
        "auth_type": {"type": "string", "enum": ["password", "key"]},
        "user": {
            "type": "string",
        },
        "password": {
            "type": "string",
        },
        "key_file": {
            "type": "string",
        },
        "watchers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["pattern", "response"],
                "properties": {
                    "pattern": {"type": "string"},
                    "response": {"type": "string"},
                },
            },
        },
    },
}


build_schema = {
    "type": "object",
    "required": ["build_set", "connection", "bricks"],
    "properties": {
        "build_set": {"type": "string"},
        "connection": connection_schema,
        "bricks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "class": {"type": "string"},
                    "module": {"type": "string"},
                    "env": {
                        "type": "object",
                    },
                    "connection": connection_schema,
                },
            },
        },
    },
}