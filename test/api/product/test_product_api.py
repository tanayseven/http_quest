from datetime import datetime

import pytest
from flask import json, Response

from http_quiz.quiz.repo import QuizRepo
from test.base import ApiTestBase
from test.fakes import FakeRandom, FakeDatetime


class TestProductApi(ApiTestBase):
    @pytest.fixture(autouse=True)
    def setup_random(self):
        FakeRandom.reset()
        self.input_range = 2
        FakeRandom.append_next_randrange(self.input_range)
        self.price = 10
        self.start_date_delta = 2
        self.end_date_delta = 2
        self.datetime_now = datetime(year=2018, month=2, day=13)
        self.add_product_parameters_to_fakers()
        self.add_product_parameters_to_fakers()

    def add_product_parameters_to_fakers(self):
        FakeRandom.append_next_randrange([self.price, self.start_date_delta, self.end_date_delta])
        FakeDatetime.set_next_dattime(self.datetime_now)

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
