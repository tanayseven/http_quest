new_password_schema = {
    'new_password': {'type': 'string', 'required': True},
}

create_new_schema = {
    'email': {'type': 'string', 'required': True},
    'password': {'type': 'string'},
}

password_reset_schema = {
    'email': {'type': 'string', 'required': True},
}
