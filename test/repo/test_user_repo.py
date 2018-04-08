import os
import pytest

from rest_test.app import app
from rest_test.extensions import db
from rest_test.model import User
from rest_test.repo import UserRepo


class DatabaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI')
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


class TestUserRepo(DatabaseTest):
    def test_authenticate_should_return_correct_user_if_user_exists(self):
        UserRepo.create_user(User(

        ))

    def test_authenticate_should_return_none_if_user_does_not_exist(self):
        pass
