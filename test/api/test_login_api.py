from flask import json

from rest_test.model import User
from rest_test.repo import UserRepo
from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def test_that_the_get_at_root_returns_correct_value(self):
        response = self.app_test.get('/')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)

    def test_that_get_at_login_returns_login_details(self):
        response = self.app_test.get('/login')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert 'login_format' in json.loads(response.data)

    def test_that_invalid_login_of_admin_with_invalid_email_fails(self):
        request_payload = {'email': 'foobaz', 'password': 'password'}
        response = self.app_test.post_json(url='/login', body=request_payload)
        assert response.status_code == 401
        assert json.loads(response.data) == {
            'description': 'Invalid credentials',
            'error': 'Bad Request',
            'status_code': 401,
        }

    def test_that_correct_login_of_admin_returns_auth_token(self):
        UserRepo.create_user(User(
            email='user@domain.com',
            password='password',
            active=True,
        ))
        request_payload = {'email': 'user@domain.com', 'password': 'password'}
        response = self.app_test.post_json(url='/login', body=request_payload)
        assert response.status_code == 200
        assert 'access_token' in json.loads(response.data)

    def test_that_correct_post_to_reset_password_succeeds(self):
        request_payload = {'email': 'user@domain.com'}
        response = self.app_test.post_json(url='/forgot_password', body=request_payload)
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
