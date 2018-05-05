from flask import json

from test.base import ApiTestBase


class TestRootApi(ApiTestBase):

    def test_that_the_get_at_root_returns_correct_value(self):
        response = self.app_test.get('/')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
