import uuid

from rest_test.user.repo import UserRepo
from test.base import DatabaseTest


class TestUserRepo(DatabaseTest):
    def test_authenticate_should_return_correct_user_if_user_exists(self):
        expected_user = self.create_user()
        actual_user = UserRepo.user_with_email_and_password('user@domain.com', 'password')
        assert expected_user == actual_user

    def test_authenticate_should_return_none_if_user_enters_wrong_email(self):
        self.create_user()
        actual_user = UserRepo.user_with_email_and_password('foobaz', 'password')
        assert actual_user is None

    def test_authenticate_should_return_none_if_user_enters_wrong_password(self):
        self.create_user()
        actual_user = UserRepo.user_with_email_and_password('user@domain.com', 'foobaz')
        assert actual_user is None

    def test_identity_should_return_user_when_given_a_user_id(self):
        user = self.create_user()
        actual_user = UserRepo.fetch_by_id(user.id)
        assert actual_user == user

    def test_identity_should_return_none_when_given_invalid_user_id(self):
        self.create_user()
        actual_user = UserRepo.fetch_by_id(12345)
        assert actual_user is None

    def test_a_new_token_should_be_stored_and_retrieved_for_a_user(self):
        user = self.create_user()
        token = str(uuid.uuid4())
        UserRepo.add_password_reset_token_to_user(user, token)
        UserRepo.reload_model(user)
        assert user.password_reset_token == token

    def test_load_user_for_email_should_return_a_user_if_it_exists(self):
        expected_user = self.create_user()
        actual_user = UserRepo.load_user_for_email(expected_user.email)
        assert expected_user == actual_user

    def test_load_user_for_email_should_not_return_a_user_if_it_does_not_exist(self):
        fetched_user = UserRepo.load_user_for_email('foobaz')
        assert fetched_user is None
