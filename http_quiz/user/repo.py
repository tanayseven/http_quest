from typing import Union, Any

from http_quiz.extensions import db
from http_quiz.user.model import User


class UserRepo:
    @staticmethod
    def add(user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def fetch_user_by_email(email: str) -> Union[User, None]:
        return db.session.query(User).\
            filter(User.email == email).one_or_none()

    @staticmethod
    def fetch_by_id(id_: int) -> Union[User, None]:
        return db.session.query(User).\
            filter(User.id == id_).one_or_none()

    @staticmethod
    def add_password_reset_token_to_user(user: User, token: str):
        user.password_reset_token = token
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def save_and_reload(obj: Any):
        db.session.add(obj)
        db.session.commit()
        db.session.refresh(obj)

    @staticmethod
    def load_user_for_email(email: str) -> User:
        return db.session.query(User).\
            filter(User.email == email).one_or_none()

    @staticmethod
    def fetch_user_by_reset_token(reset_token: str) -> User:
        return db.session.query(User).\
            filter(User.password_reset_token == reset_token).one_or_none()
