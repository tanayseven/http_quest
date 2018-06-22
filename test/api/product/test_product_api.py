from datetime import datetime

import pytest
from flask import json, Response

from http_quiz.product_quiz.problem_statements import Product
from http_quiz.quiz.repo import QuizRepo
from test.base import ApiTestBase
from test.fakes import FakeRandom, FakeDatetime


class TestProductApi(ApiTestBase):
    @pytest.fixture(autouse=True)
    def setup_random(self):
        FakeRandom.reset()
        self.init_faker_for_input_api_call()

    def init_faker_for_input_api_call(self):
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

    def answer_first_question(self, answer_correct_solution=True):
        self.candidate_token = self.create_candidate()
        self.response_for_input(problem_number=1, auth_token=self.candidate_token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        solution = {} if not answer_correct_solution else problem_input_output.output
        response = self.response_for_output(1, auth_token=self.candidate_token, body=solution)
        return response

    def answer_second_question(self, answer_correct_solution=True):
        self.app_test.get('product_quiz/problem_statement', headers={'Authorization': self.candidate_token})
        self.init_faker_for_input_api_call()
        self.response_for_input(problem_number=2, auth_token=self.candidate_token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        solution = {} if not answer_correct_solution else problem_input_output.output
        response = self.response_for_output(2, auth_token=self.candidate_token, body=solution)
        return response

    def answer_third_question(self, answer_correct_solution=True):
        self.app_test.get('product_quiz/problem_statement', headers={'Authorization': self.candidate_token})
        self.init_faker_for_input_api_call()
        self.response_for_input(problem_number=3, auth_token=self.candidate_token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        solution = {} if not answer_correct_solution else problem_input_output.output
        response = self.response_for_output(3, auth_token=self.candidate_token, body=solution)
        return response

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
        assert problem_input_output.input == json.loads(input_response.data)

    def test_answer_to_first_problem_if_correct_should_be_reflected_in_the_db(self):
        response = self.answer_first_question()
        assert response.status_code == 200
        assert 'You\'ve solved this problem successfully.' in response.data.decode()
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert problem_input_output.has_been_solved(1)

    def test_answer_to_first_problem_if_wrong_should_be_return_appropriate_response(self):
        response = self.answer_first_question(answer_correct_solution=False)
        assert response.status_code == 400
        assert 'Wrong solution.' in response.data.decode()
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert not problem_input_output.has_been_solved(1)

    def test_answer_to_the_first_problem_if_wrong_should_ask_to_fetch_new_input(self):
        self.answer_first_question(answer_correct_solution=False)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        solution = Product.solution_count(problem_input_output.input)
        response = self.response_for_output(1, auth_token=self.candidate_token, body=solution)
        assert 'already attempted' in response.data.decode()

    def test_that_the_get_problem_statement_after_answering_first_problem_shows_second_problem(self):
        self.answer_first_question()
        response = self.app_test.get('product_quiz/problem_statement', headers={'Authorization': self.candidate_token})
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        assert 'This problem number is 2' in response.data.decode()
        self.init_faker_for_input_api_call()
        input_response = self.response_for_input(problem_number=2, auth_token=self.candidate_token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert input_response.status_code == 200
        assert problem_input_output.input == json.loads(input_response.data)

    def test_answer_to_second_problem_if_correct_should_be_reflected_in_the_db(self):
        self.answer_first_question()
        response = self.answer_second_question()
        assert response.status_code == 200
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert problem_input_output.has_been_solved(2)

    def test_answer_to_second_problem_if_wrong_should_be_return_appropriate_response(self):
        self.answer_first_question()
        response = self.answer_second_question(answer_correct_solution=False)
        assert response.status_code == 400
        assert 'Wrong solution.' in response.data.decode()
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert not problem_input_output.has_been_solved(2)

    def test_that_the_get_problem_statement_after_answering_second_problem_shows_third_problem(self):
        self.answer_first_question()
        self.answer_second_question()
        response = self.app_test.get('product_quiz/problem_statement', headers={'Authorization': self.candidate_token})
        assert 'message' in json.loads(response.data)
        assert 'This problem number is 3' in response.data.decode()
        self.init_faker_for_input_api_call()
        input_response = self.response_for_input(problem_number=3, auth_token=self.candidate_token)
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert input_response.status_code == 200
        assert problem_input_output.input == json.loads(input_response.data)

    def test_answer_to_third_problem_if_correct_should_be_reflected_in_the_db(self):
        self.answer_first_question()
        self.answer_second_question()
        response = self.answer_third_question()
        assert response.status_code == 200
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert problem_input_output.has_been_solved(3)

    def test_answer_to_third_problem_if_wrong_should_be_return_appropriate_response(self):
        self.answer_first_question()
        self.answer_second_question()
        response = self.answer_third_question(answer_correct_solution=False)
        assert response.status_code == 400
        assert 'Wrong solution.' in response.data.decode()
        problem_input_output = QuizRepo.fetch_latest_answer_by_candidate(self.candidate)
        assert not problem_input_output.has_been_solved(3)

    @pytest.mark.skip()
    def test_that_the_get_problem_statement_after_answering_third_problem_shows_fourth_problem(self):
        pass

    @pytest.mark.skip()
    def test_answer_to_fourth_problem_if_correct_should_be_reflected_in_the_db(self):
        pass

    @pytest.mark.skip()
    def test_answer_to_fourth_problem_if_wrong_should_be_return_appropriate_response(self):
        pass

    @pytest.mark.skip()
    def test_that_the_get_problem_statement_after_answering_fourth_problem_shows_completion(self):
        pass

    def response_for_input(self, problem_number: int, auth_token) -> Response:
        return self.app_test.get(
            'product_quiz/{0}/input'.format(problem_number),
            headers={'Authorization': auth_token},
        )

    def response_for_output(self, problem_number: int, auth_token, body) -> Response:
        return self.app_test.post_json(
            'product_quiz/{0}/output'.format(problem_number),
            headers={'Authorization': auth_token},
            body=body,
        )
