import uuid
from typing import Tuple, Union

from flask_babel import gettext as _
from flask_mail import Message

from http_quest.di import container
from http_quest.ext import mail
from http_quest.user.model import User
from http_quest.user.repo import UserRepo
from http_quest.utilities import load_template


def authenticate(email: str, password: str) -> Union[User, None]:
    user = UserRepo.fetch_user_by_email(email)
    if user is None:
        return None
    password_matches = container.bcrypt.check_password_hash(user.password, password)
    return user if password_matches else None


def update_password_for_token(reset_token: str, password: str) -> bool:
    user = UserRepo.fetch_user_by_reset_token(reset_token)
    if user is not None:
        user.password = container.bcrypt.generate_password_hash(password).decode()
        user.password_reset_token = None
        UserRepo.save_and_reload(user)
        return True
    return False


def create_user(email: str, password: str = None) -> bool:
    hashed_password, success = _generate_hashed_password_if_user_email_does_not_exist(email, password)
    if not success:
        return success
    user = UserRepo.add(User(email=email, password=hashed_password))
    _reset_password_for_user(user)
    return True


def _generate_hashed_password_if_user_email_does_not_exist(email: str, password: str):
        success = True
        hashed_password = None
        existing_user = UserRepo.fetch_user_by_email(email)
        if existing_user is not None:
            success = False
        if password is not None:
            hashed_password = container.bcrypt.generate_password_hash(password).decode()
        return hashed_password, success


def identity(payload: dict):
    return UserRepo.fetch_by_id(payload.get('identity'))


def reset_password_for_user_having_email(email: str) -> Tuple[dict, bool]:
    user = UserRepo.load_user_for_email(email)
    if user is None:
        return {'message': _('User could not be found')}, False
    _reset_password_for_user(user)
    return {'message': _('Password reset instructions successfully sent to your email address')}, True


def _reset_password_for_user(user: User):
    token = _create_password_reset_token(user)
    msg = Message(
        _('Password Reset Instructions'),
        recipients=[user.email],
        body=load_template('password_reset.html', {'token': token}),
    )
    mail.send(msg)


def _create_password_reset_token(user: User) -> str:
    token = str(uuid.uuid4())
    UserRepo.add_password_reset_token_to_user(user, token)
    return token
