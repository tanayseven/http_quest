from functools import wraps

import os
from cerberus import Validator
from flask import request, jsonify


def get_translation_for(strings: dict, key: str) -> str:
    return strings.get(
        request.headers.get('Accept-Language') and request.headers.get('Accept-Language').split(',')[0]
        or 'en_IN'
    ) or strings.get(os.environ.get('APP_LOCALE')).get(key)


def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if Validator(schema).validate(request.json):
                return f(*args, **kwargs)
            return jsonify({'message': 'Invalid json'}), 400
        return decorated_function
    return decorator
