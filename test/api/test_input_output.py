import requests

from test.base import ApiTestBase


class TestInputApi(ApiTestBase):

    def test_that_the_get_at_root_returns_correct_value(self):
        response = requests.get(self.get_server_url())
        assert response.status_code == 200
        assert response.json() == {'message': 'this is the / please go to /login for any further activity'}

    def test_that_post_also_works_as_well(self):
        response = requests.post(self.get_server_url() + '/send', json={'something': 'lala'})
        assert response.status_code == 200
        assert response.json() == {'something': 'something extra'}

    def test_that_get_at_login_returns_login_details(self):
        response = requests.get(self.get_server_url() + '/login')
        assert response.status_code == 200
        assert response.json() == {
            'message': 'to login, please POST `login_format` on /login',
            'login_format': {'email': '<your_email>', 'password': '<your_password>'}
        }
