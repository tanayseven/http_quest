import uuid

from http_quiz.user.repo import UserRepo
from test.base import DatabaseTest


class TestUserRepo(DatabaseTest):

    def test_authenticate_should_return_correct_user_if_user_exists(self):
        expected_user = UserRepo.add(self.new_user())
        actual_user = UserRepo.fetch_user_by_email('user@domain.com')
        assert expected_user == actual_user

    def test_authenticate_should_return_none_if_user_enters_wrong_email(self):
        _ = UserRepo.add(self.new_user())
        actual_user = UserRepo.fetch_user_by_email('foobaz')
        assert actual_user is None

    def test_identity_should_return_user_when_given_a_user_id(self):
        expected_user = UserRepo.add(self.new_user())
        actual_user = UserRepo.fetch_by_id(expected_user.id)
        assert actual_user == expected_user

    def test_identity_should_return_none_when_given_invalid_user_id(self):
        _ = UserRepo.add(self.new_user())
        actual_user = UserRepo.fetch_by_id(12345)
        assert actual_user is None

    def test_a_new_token_should_be_stored_and_retrieved_for_a_user(self):
        user = UserRepo.add(self.new_user())
        token = str(uuid.uuid4())
        UserRepo.add_password_reset_token_to_user(user, token)
        UserRepo.save_and_reload(user)
        assert user.password_reset_token == token

    def test_load_user_for_email_should_return_a_user_if_it_exists(self):
        expected_user = UserRepo.add(self.new_user())
        actual_user = UserRepo.load_user_for_email(expected_user.email)
        assert expected_user == actual_user

    def test_load_user_for_email_should_not_return_a_user_if_it_does_not_exist(self):
        fetched_user = UserRepo.load_user_for_email('foobaz')
        assert fetched_user is None

    def test_fetch_user_by_reset_token_should_return_the_correct_user(self):
        UserRepo.add(self.new_user('user1@domain.com'))
        expected_user = UserRepo.add(self.new_user())
        UserRepo.add(self.new_user('user2@domain.com'))
        token = str(uuid.uuid4())
        expected_user.password_reset_token = token
        UserRepo.save_and_reload(expected_user)
        actual_user = UserRepo.fetch_user_by_reset_token(token)
        assert actual_user == expected_user
