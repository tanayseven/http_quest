from typing import Union

from rest_test.extensions import db, jwt
from rest_test.model import User


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
    def identity(cls, payload: str) -> Union[User, None]:
        pass
