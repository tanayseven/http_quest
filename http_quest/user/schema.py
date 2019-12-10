new_password_schema = {
    'type': 'object',
    'required': ['new_password'],
    'properties': {
        'new_password': {'type': 'string'},
    },
    "additionalProperties": False,
}

create_new_schema = {
    'type': 'object',
    'required': ['email'],
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'},
    },
    "additionalProperties": False,
}

password_reset_schema = {
    'type': 'object',
    'required': ['email'],
    'properties': {
        'email': {'type': 'string'},
    },
    "additionalProperties": False,
}
