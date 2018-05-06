from typing import Union

from rest_test.extensions import db
from rest_test.user.model import User


class UserRepo:
    @staticmethod
    def create_user(user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate(email: str, password: str) -> Union[User, None]:
        return db.session.query(User).\
            filter_by(email=email, password=password).one_or_none()

    @staticmethod
    def identity(payload: dict) -> Union[User, None]:
        return db.session.query(User).\
            filter_by(id=payload.get('identity')).one_or_none()
