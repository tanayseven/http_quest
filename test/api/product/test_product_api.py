import pytest
from flask import json

from test.base import ApiTestBase


class TestProductsApi(ApiTestBase):

    def test_that_the_get_at_root_of_products_returns_correct_value(self):
        response = self.app_test.get('product_quiz/')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)

    @pytest.mark.skip()
    def test_that_the_get_at_problem_statement_shows_the_first_problem_when_none_are_yet_answered(self):
        token = self.create_candidate()
        response = self.app_test.get('product_quiz/problem_statement/', headers={'Authorization': token})
        # TODO complete this test
