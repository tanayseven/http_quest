from flask import json

from rest_test.user.model import User
from rest_test.user.repo import UserRepo
from rest_test.user.translations import get_text
from rest_test.user.user import create_user
from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def request_login(self, user: User) -> str:
        request_payload = {'email': user.email, 'password': 'password'}
        response = self.app_test.post_json(url='/user/login', body=request_payload)
        token = 'JWT ' + json.loads(response.data)['access_token']
        return token

    def test_that_correct_post_to_reset_password_succeeds(self):
        user = self.create_user()
        request_payload = {'email': user.email}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert len(self.mail_outbox) == 1
        assert self.mail_outbox[0].subject == get_text('password_reset_mail_subject')

    def test_that_invalid_email_sent_to_reset_password_fails(self):
        request_payload = {'email': 'foo baz'}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        assert response.status_code == 404
        assert 'message' in json.loads(response.data)

    def test_that_a_user_who_had_logged_in_can_create_other_users_successfully(self):
        token = self.request_login(self.create_user())
        response = self.app_test.post_json(
            url='/user/create_new',
            body={'email': 'someuser@somedomain.com'},
            headers={'Authorization': token},
        )
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert len(self.mail_outbox) == 1
        assert self.mail_outbox[0].recipients == ['someuser@somedomain.com']
        assert self.mail_outbox[0].subject == get_text('password_reset_mail_subject')
        expected_user = UserRepo.fetch_user_by_email('someuser@somedomain.com')
        assert expected_user is not None

    def test_that_new_user_should_not_be_created_if_it_already_exists(self):
        token = self.request_login(self.create_user())
        create_user('someuser@somedomain.com', 'password')
        response = self.app_test.post_json(
            url='/user/create_new',
            body={'email': 'someuser@somedomain.com'},
            headers={'Authorization': token},
        )
        assert response.status_code == 400
        assert 'message' in json.loads(response.data)
