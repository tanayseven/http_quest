from flask import json

from http_quiz.user.repo import UserRepo
from test.base import ApiTestBase


class TestAuthApi(ApiTestBase):

    def test_that_get_at_login_returns_login_details(self):
        response = self.app_test.get('/user/login')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert 'login_format' in json.loads(response.data)

    def test_that_invalid_login_of_admin_with_invalid_email_fails(self):
        request_payload = {'email': 'foobaz', 'password': 'password'}
        response = self.app_test.post_json(url='/user/login', body=request_payload)
        assert response.status_code == 401
        assert json.loads(response.data) == {
            'description': 'Invalid credentials',
            'error': 'Bad Request',
            'status_code': 401,
        }

    def test_that_correct_login_of_admin_returns_auth_token(self):
        UserRepo.add(self.new_user())
        request_payload = {'email': 'user@domain.com', 'password': 'password'}
        response = self.app_test.post_json(url='/user/login', body=request_payload)
        assert response.status_code == 200
        assert 'access_token' in json.loads(response.data)
