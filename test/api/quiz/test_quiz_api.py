from flask import json

from http_quest.quiz.model import QuizType
from http_quest.quiz.repo import CandidateRepo
from http_quest.quiz.translations import get_text
from test.base import ApiTestBase


class TestQuizApi(ApiTestBase):
    def test_creation_of_new_candidate_token_should_successfully_send_emails_to_two_recipients(self):
        user = self.create_user()
        token = self.request_login_token(self.app_test, user)
        body = self.sample_quiz_creation_body()
        headers = {'Authorization': token}
        response = self.app_test.post_json(url='/quiz/new_candidate_token', body=body, headers=headers)
        assert response.status_code == 200
        self.assert_has_one_mail_with_subject_and_recipients(
            get_text('candidate_token_mail_subject'),
            [body.get('email'), user.email]
        )
        candidate_token = self.mail_body_extract_token()
        candidate = CandidateRepo.fetch_candidate_by_token(candidate_token)
        assert candidate.email == 'candidate@domain.com'

    def test_list_quiz_type_returns_list_of_all_quizzes(self):
        token = self.request_login_token(self.app_test, self.create_user())
        headers = {'Authorization': token}
        response = self.app_test.get('/quiz/list_quiz_types', headers=headers)
        assert response.status_code == 200
        response_json = json.loads(response.data)
        assert response_json.get('list_quiz_types') == [str(type_) for type_ in QuizType]
