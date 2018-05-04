import requests

from rest_test.model import User
from rest_test.repo import UserRepo
from test.base import ApiTestBase, DatabaseTest


class TestLoginApi(DatabaseTest, ApiTestBase):

    def test_that_the_get_at_root_returns_correct_value(self):
        response = requests.get(self.get_server_url())
        assert response.status_code == 200
        assert 'message' in response.json()

    def test_that_get_at_login_returns_login_details(self):
        response = requests.get(self.get_server_url() + '/login')
        assert response.status_code == 200
        assert response.json() == {
            'message': 'to login, please POST `login_format` on /login',
            'login_format': {'email': '<your_email>', 'password': '<your_password>'}
        }

    def test_that_invalid_login_of_admin_with_invalid_email_fails(self):
        request_payload = {'email': 'foobaz', 'password': 'password'}
        response = requests.post(self.get_server_url() + '/login', json=request_payload)
        assert response.status_code == 401
        assert response.json() == {
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
        response = requests.post(self.get_server_url() + '/login', json=request_payload)
        assert response.status_code == 200
        assert 'access_token' in response.json()
