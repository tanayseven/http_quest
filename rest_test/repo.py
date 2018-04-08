from typing import Union

from rest_test.model import User


class UserRepo:
    model = User

    @staticmethod
    def create_user(user: User):
        pass

    @staticmethod
    def authenticate(username: str, password: str) -> Union[User, None]:
        pass

    @staticmethod
    def identity(payload: str) -> Union[User, None]:
        pass
