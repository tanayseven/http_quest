import os
from flask import request


def get_translation_for(strings: dict, key: str) -> str:
    return strings.get(
        request.headers.get('Accept-Language') and request.headers.get('Accept-Language').split(',')[0]
        or 'en_IN'
    ) or strings.get(os.environ.get('APP_LOCALE')).get(key)
