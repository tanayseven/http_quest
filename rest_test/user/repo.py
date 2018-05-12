from typing import Union, Any

from rest_test.extensions import db
from rest_test.user.model import User


class UserRepo:
    @staticmethod
    def add(user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def fetch_user_by_email(email: str) -> Union[User, None]:
        return db.session.query(User).\
            filter_by(email=email).one_or_none()

    @staticmethod
    def fetch_by_id(id_: int) -> Union[User, None]:
        return db.session.query(User).\
            filter_by(id=id_).one_or_none()

    @staticmethod
    def add_password_reset_token_to_user(user: User, token: str):
        user.password_reset_token = token
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def reload(obj: Any):
        db.session.refresh(obj)

    @staticmethod
    def load_user_for_email(email: str):
        return db.session.query(User).\
            filter_by(email=email).one_or_none()
