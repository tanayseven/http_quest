from flask import json

from test.base import ApiTestBase


class TestProductsApi(ApiTestBase):

    def test_that_the_get_at_root_of_products_returns_correct_value(self):
        response = self.app_test.get('product/')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
