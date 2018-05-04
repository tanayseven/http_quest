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

    def test_identity_should_return_user_when_given_a_user_id(self):
        user = UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        actual_user = UserRepo.identity({'id': user.id})
        assert actual_user == user

    def test_identity_should_return_none_when_given_invalid_user_id(self):
        UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        actual_user = UserRepo.identity({'id': 12345})
        assert actual_user is None
