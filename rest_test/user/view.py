from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required

from rest_test.user.translations import get_text
from rest_test.user.user import reset_password_for_user_having_email, create_user

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': get_text('login_instruction'),
        'login_format': {'email': get_text('your_email'), 'password': get_text('your_password')}
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
        'message': get_text('user_created'),
    }
    success = create_user(request.json.get('email'), request.json.get('password'))
    if success:
        return jsonify(success_data)
    else:
        return jsonify({'message': get_text('user_already_exists')}), 400
