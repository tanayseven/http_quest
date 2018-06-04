import uuid
from typing import Tuple, Union

from flask_bcrypt import Bcrypt
from flask_mail import Message
from injector import inject

from http_quiz.di import injector
from http_quiz.extensions import mail
from http_quiz.user.model import User
from http_quiz.user.repo import UserRepo
from http_quiz.user.translations import get_text
from http_quiz.utilities import load_template


class BcryptAuth:
    @inject
    def __init__(self, bcrypt: Bcrypt):
        self.bcrypt = bcrypt

    def authenticate(self, email: str, password: str) -> Union[User, None]:
        user = UserRepo.fetch_user_by_email(email)
        if user is None:
            return None
        password_matches = self.bcrypt.check_password_hash(user.password, password)
        return user if password_matches else None

    def update_password_for_token(self, reset_token: str, password: str) -> bool:
        user = UserRepo.fetch_user_by_reset_token(reset_token)
        if user is not None:
            user.password = self.bcrypt.generate_password_hash(password).decode()
            user.password_reset_token = None
            UserRepo.save_and_reload(user)
            return True
        return False

    def create_user(self, email: str, password: str = None) -> bool:
        hashed_password, success = self._generate_hashed_password_if_user_email_does_not_exist(email, password)
        if not success:
            return success
        user = UserRepo.add(User(email=email, password=hashed_password))
        _reset_password_for_user(user)
        return True

    def _generate_hashed_password_if_user_email_does_not_exist(self, email: str, password: str):
        success = True
        hashed_password = None
        existing_user = UserRepo.fetch_user_by_email(email)
        if existing_user is not None:
            success = False
        if password is not None:
            hashed_password = self.bcrypt.generate_password_hash(password).decode()
        return hashed_password, success


bcrypt_auth: BcryptAuth = injector.get(BcryptAuth)


def identity(payload: dict):
    return UserRepo.fetch_by_id(payload.get('identity'))


def reset_password_for_user_having_email(email: str) -> Tuple[dict, bool]:
    user = UserRepo.load_user_for_email(email)
    if user is None:
        return {'message': get_text('user_not_found')}, False
    _reset_password_for_user(user)
    return {'message': get_text('password_reset_instructions_sent_to_email')}, True


def _reset_password_for_user(user: User):
    token = _create_password_reset_token(user)
    msg = Message(
        get_text('password_reset_mail_subject'),
        recipients=[user.email],
        body=load_template('password_reset.html', {'token': token}),
    )
    mail.send(msg)


def _create_password_reset_token(user: User) -> str:
    token = str(uuid.uuid4())
    UserRepo.add_password_reset_token_to_user(user, token)
    return token
