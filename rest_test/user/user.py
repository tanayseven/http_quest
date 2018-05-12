import uuid
from typing import Tuple, Union

from flask_mail import Message

from rest_test.extensions import mail
from rest_test.user.model import User
from rest_test.user.repo import UserRepo
from rest_test.user.translations import get_text


def reset_password_for_user_having_email(email: str) -> Tuple[dict, bool]:
    user = UserRepo.load_user_for_email(email)
    if user is None:
        return {'message': get_text('user_not_found')}, False
    token = create_password_reset_token(user)
    msg = Message(
        get_text('password_reset_mail_subject'),
        recipients=[user.email],
        body=str({
            'message': get_text('password_reset_mail_message'),
            'token': token,
            'json_format': {
                'new_password': '<password>',
            },
        }))
    mail.send(msg)
    return {'message': get_text('password_reset_instructions_sent_to_email')}, True


def create_password_reset_token(user: User) -> str:
    token = str(uuid.uuid4())
    UserRepo.add_password_reset_token_to_user(user, token)
    return token


def authenticate(email: str, password: str) -> Union[User, None]:
    # TODO add bcrypt logic here
    return UserRepo.user_with_email_and_password(email, password)


def identity(payload: dict):
    return UserRepo.fetch_by_id(payload.get('identity'))
