from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required

from http_quiz.user.schema import new_password_schema, create_new_schema, password_reset_schema
from http_quiz.user.translations import get_text
from http_quiz.user.user import reset_password_for_user_having_email, bcrypt_auth
from http_quiz.utilities import validate_json

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': get_text('login_instruction'),
        'login_format': {'email': get_text('your_email'), 'password': get_text('your_password')}
    }
    return jsonify(data)


@user_view.route('/user/forgot_password', methods=('POST',))
@validate_json(password_reset_schema)
def password_reset():
    message, success = reset_password_for_user_having_email(request.json.get('email'))
    if not success:
        return jsonify(message), 404
    return jsonify(message)


@user_view.route('/user/create_new', methods=('POST',))
@jwt_required()
@validate_json(create_new_schema)
def create_new():
    success_data = {
        'message': get_text('user_created'),
    }
    success = bcrypt_auth.create_user(request.json.get('email'), request.json.get('password'))
    if success:
        return jsonify(success_data)
    return jsonify({'message': get_text('user_already_exists')}), 400


@user_view.route('/user/new_password/<reset_token>', methods=('POST',))
@validate_json(new_password_schema)
def new_password(reset_token: str):
    success_response = {
        'message': get_text('password_successfully_reset')
    }
    success = bcrypt_auth.update_password_for_token(reset_token, request.json.get('new_password'))
    if success:
        return jsonify(success_response), 200
    return jsonify({'message': get_text('invalid_password_token')}), 400
