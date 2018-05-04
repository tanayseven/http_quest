from flask import Blueprint, jsonify

root_view = Blueprint('root', __name__)


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
