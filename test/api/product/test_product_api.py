import pytest
from flask import json, Response

from http_quiz.quiz.repo import QuizRepo
from test.base import ApiTestBase


class TestProductApi(ApiTestBase):

    def test_that_the_get_at_root_of_products_returns_correct_value(self):
        response = self.app_test.get('product_quiz/')
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)

    def test_that_the_get_at_problem_statement_shows_the_first_problem_when_none_are_yet_answered(self):
        token = self.create_candidate()
        response = self.app_test.get('product_quiz/problem_statement', headers={'Authorization': token})
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert 'This problem number is 1' in response.data.decode()
        input_response = self.response_for_input(problem_number=1, auth_token=token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert input_response.status_code == 200
        assert problem_input_output[1].input == json.loads(input_response.data)

    def response_for_input(self, problem_number: int, auth_token) -> Response:
        return self.app_test.get(
            'product_quiz/{0}/input'.format(problem_number),
            headers={'Authorization': auth_token}
        )
