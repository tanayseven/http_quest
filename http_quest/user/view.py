from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from flask_babel import gettext as _

from http_quest.user.schema import new_password_schema, create_new_schema, password_reset_schema
from http_quest.user.user import reset_password_for_user_having_email, create_user, update_password_for_token
from http_quest.utilities import validate_json

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': _('To login, please POST `login_format` on /login'),
        'login_format': {'email': _('<your_email>'), 'password': _('<your_password>')}
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
        'message': _('The user has been created and the password information is sent to them'),
    }
    success = create_user(request.json.get('email'), request.json.get('password'))
    if success:
        return jsonify(success_data)
    return jsonify({'message': _('The user already exists')}), 400


@user_view.route('/user/new_password/<reset_token>', methods=('POST',))
@validate_json(new_password_schema)
def new_password(reset_token: str):
    success_response = {
        'message': _('Your password has been successfully reset.')
    }
    success = update_password_for_token(reset_token, request.json.get('new_password'))
    if success:
        return jsonify(success_response), 200
    return jsonify({'message': _('You have submitted an invalid password token.')}), 400
