from flask import json

from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def test_that_correct_post_to_reset_password_succeeds(self):
        request_payload = {'email': 'user@domain.com'}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
