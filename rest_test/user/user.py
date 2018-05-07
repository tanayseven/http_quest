from typing import Tuple

from flask_mail import Message

from rest_test.extensions import mail
from rest_test.user.repo import UserRepo


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