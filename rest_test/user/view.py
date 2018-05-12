from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required

from rest_test.user.user import reset_password_for_user_having_email, create_user

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': 'to login, please POST `login_format` on /login',
        'login_format': {'email': '<your_email>', 'password': '<your_password>'}
    }
    return jsonify(data)


@user_view.route('/user/forgot_password', methods=('POST',))
def password_reset():
    message, success = reset_password_for_user_having_email(request.json.get('email'))
    if not success:
        return jsonify(message), 404
    return jsonify(message)


@user_view.route('/user/create_new', methods=('POST',))
@jwt_required()
def create_new():
    success_data = {
        'message': 'the user has been created and the password information is sent to them',
    }
    success = create_user(request.json.get('email'), request.json.get('password'))
    if success:
        return jsonify(success_data)
    else:
        return jsonify({'message': 'the user already exists'}), 400
