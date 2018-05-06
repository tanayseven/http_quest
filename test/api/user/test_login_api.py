from flask import json

from rest_test.extensions import mail
from rest_test.user.model import User
from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def request_login(self, user: User) -> str:
        request_payload = {'email': user.email, 'password': user.password}
        response = self.app_test.post_json(url='/user/login', body=request_payload)
        token = 'JWT ' + json.loads(response.data)['access_token']
        return token

    def test_that_correct_post_to_reset_password_succeeds(self):
        request_payload = {'email': 'user@domain.com'}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        assert len(self.mail_outbox) == 1
        assert response.status_code == 200
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
