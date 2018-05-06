from rest_test.user.model import User
from rest_test.user.repo import UserRepo
from test.base import DatabaseTest


class TestUserRepo(DatabaseTest):
    def test_authenticate_should_return_correct_user_if_user_exists(self):
        expected_user = self.create_user()
        actual_user = UserRepo.authenticate('user@domain.com', 'password')
        assert expected_user == actual_user

    def test_authenticate_should_return_none_if_user_enters_wrong_email(self):
        self.create_user()
        actual_user = UserRepo.authenticate('foobaz', 'password')
        assert actual_user is None

    def test_authenticate_should_return_none_if_user_enters_wrong_password(self):
        self.create_user()
        actual_user = UserRepo.authenticate('user@domain.com', 'foobaz')
        assert actual_user is None

    def test_identity_should_return_user_when_given_a_user_id(self):
        user = self.create_user()
        actual_user = UserRepo.identity({'identity': user.id})
        assert actual_user == user

    def test_identity_should_return_none_when_given_invalid_user_id(self):
        self.create_user()
        actual_user = UserRepo.identity({'id': 12345})
        assert actual_user is None

    def test_a_new_token_should_be_stored_and_retrieved_for_a_user(self):
        user = self.create_user()
        token = UserRepo.create_password_reset_token(user)
        UserRepo.reload_model(user)
        assert user.password_reset_token == token
