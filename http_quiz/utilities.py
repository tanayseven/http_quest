from functools import wraps

import os
from cerberus import Validator
from flask import request, jsonify


def get_translation_for(strings: dict, key: str) -> str:
    return strings.get(
        fetch_locale_from_request_else_use_default()
    ).get(key)


def fetch_locale_from_request_else_use_default():
    return (
        request.headers.get('Accept-Language') and request.headers.get('Accept-Language').split(',')[0]
        or os.environ.get('APP_LOCALE')
    )


def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if Validator(schema).validate(request.json):
                return f(*args, **kwargs)
            return jsonify({'message': 'Invalid json'}), 400

        return decorated_function

    return decorator
