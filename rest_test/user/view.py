from typing import Tuple

from flask import jsonify, Blueprint, request
from flask_jwt import jwt_required
from flask_mail import Message

from rest_test.extensions import mail
from rest_test.user.repo import UserRepo

user_view = Blueprint('user', __name__)


@user_view.route('/user/login', methods=('GET',))
def login_get():
    data = {
        'message': 'to login, please POST `login_format` on /login',
        'login_format': {'email': '<your_email>', 'password': '<your_password>'}
    }
    return jsonify(data)


def reset_password_for_user_having_email(email: str) -> Tuple[dict, bool]:
    user = UserRepo.load_user_for_email(email)
    if user is None:
        return {'message': 'user not found'}, False
    token = UserRepo.create_password_reset_token(user)
    msg = Message(
        'Password Reset Instructions',
        recipients=[user.email],
        body=str({
            'message': 'use this token to reset your password, send a json_format to /user/new_password/<reset_token>',
            'token': token,
            'json_format': {
                'new_password': '<password>',
            },
        }))
    mail.send(msg)
    return {'message': 'password reset instructions successfully sent to your email address'}, True


@user_view.route('/user/forgot_password', methods=('POST',))
def password_reset():
    data = {
        'message': 'you should have received an email with password reset instructions',
    }
    message, success = reset_password_for_user_having_email(request.json.get('email'))
    if not success:
        return jsonify(data), 404
    return jsonify(data)



@user_view.route('/user/create_new', methods=('POST',))
@jwt_required()
def create_new():
    success_data = {
        'message': 'the user has been created and the password information is sent to them',
    }
    return jsonify(success_data)
