from typing import Tuple

from flask import Blueprint, jsonify, request

root_view = Blueprint('root', __name__)


def login_user(username: str, password: str) -> Tuple[bool, str]:
    return False, ''


@root_view.route('/', methods=('GET',))
def root_get():
    data = {'message': 'this is the / please go to /login for any further activity'}
    return jsonify(data)


@root_view.route('/login', methods=('GET',))
def login_get():
    data = {
        'message': 'to login, please POST `login_format` on /login',
        'login_format': {'email': '<your_email>', 'password': '<your_password>'}
    }
    return jsonify(data)


@root_view.route('/send', methods=('POST',))
def something_else():
    data = {'something': 'something extra'}
    return jsonify(data)
