import os
from functools import wraps

from cerberus import Validator
from flask import request, jsonify, render_template


def fetch_locale_from_request_else_use_default():
    return (
            request and request.headers.get('Accept-Language') and request.headers.get('Accept-Language').split(',')[0]
            or os.environ.get('APP_LOCALE')
    )


def get_translation_for(strings: dict, key: str) -> str:
    return strings.get(
        fetch_locale_from_request_else_use_default()
    ).get(key)


def load_template(template_name: str, args: dict):
    return render_template(fetch_locale_from_request_else_use_default() + '/' + template_name, **args)


def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if Validator(schema).validate(request.json):
                return f(*args, **kwargs)
            return jsonify({'message': 'Invalid json'}), 400

        return decorated_function

    return decorator
