from flask import json

from rest_test.user.model import User
from rest_test.user.translations import get_text
from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def request_login(self, user: User) -> str:
        request_payload = {'email': user.email, 'password': user.password}
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

    def test_that_a_user_who_had_logged_in_can_create_other_users(self):
        token = self.request_login(self.create_user())
        response = self.app_test.post_json(
            url='/user/create_new',
            body={'email': 'someuser@somedomain.com'},
            headers={'Authorization': token},
        )
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
