from rest_test.model import User
from rest_test.repo import UserRepo
from test.base import DatabaseTest


class TestUserRepo(DatabaseTest):
    def test_authenticate_should_return_correct_user_if_user_exists(self):
        expected_user = UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        actual_user = UserRepo.authenticate('user@domain.com', 'password')
        assert expected_user == actual_user

    def test_authenticate_should_return_none_if_user_enters_wrong_email(self):
        UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        actual_user = UserRepo.authenticate('foobaz', 'password')
        assert None == actual_user

    def test_authenticate_should_return_none_if_user_enters_wrong_password(self):
        UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        actual_user = UserRepo.authenticate('user@domain.com', 'foobaz')
        assert None == actual_user
