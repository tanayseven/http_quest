from flask import json

from rest_test.user.repo import UserRepo
from rest_test.user.translations import get_text
from rest_test.user.user import create_user
from test.base import ApiTestBase


class TestLoginApi(ApiTestBase):

    def test_that_correct_post_to_reset_password_succeeds(self):
        user = self.create_user()
        request_payload = {'email': user.email}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        self.assert_response_ok_and_has_message(response)
        subject = get_text('password_reset_mail_subject')
        self.assert_has_one_mail_with_subject(subject)

    def test_that_invalid_email_sent_to_reset_password_fails(self):
        request_payload = {'email': 'foo baz'}
        response = self.app_test.post_json(url='/user/forgot_password', body=request_payload)
        assert response.status_code == 404
        assert 'message' in json.loads(response.data)

    def test_that_on_sending_invalid_json_create_other_user_fails(self):
        token = self.request_login_token(self.app_test, self.create_user())
        response = self.app_test.post_json(
            url='/user/create_new',
            body={},
            headers={'Authorization': token},
        )
        assert response.status_code == 400

    def test_that_a_user_who_had_logged_in_can_create_other_users_successfully(self):
        token = self.request_login_token(self.app_test, self.create_user())
        response = self.app_test.post_json(
            url='/user/create_new',
            body={'email': 'someuser@somedomain.com'},
            headers={'Authorization': token},
        )
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)
        self.assert_has_one_mail_with_subject_and_recipients(
            subject=get_text('password_reset_mail_subject'),
            recipients=['someuser@somedomain.com'],
        )
        expected_user = UserRepo.fetch_user_by_email('someuser@somedomain.com')
        assert expected_user is not None

    def test_that_new_user_should_not_be_created_if_it_already_exists(self):
        token = self.request_login_token(self.app_test, self.create_user())
        create_user('someuser@somedomain.com', 'password')
        response = self.app_test.post_json(
            url='/user/create_new',
            body={'email': 'someuser@somedomain.com'},
            headers={'Authorization': token},
        )
        assert response.status_code == 400
        assert 'message' in json.loads(response.data)

    def test_that_an_existing_user_who_has_reset_password_can_set_a_new_one(self):
        user = self.create_user()
        self.app_test.post_json(
            url='/user/forgot_password',
            body={'email': user.email},
        )
        password_reset_token = self.mail_body_json().get('token')
        response = self.app_test.post_json(
            url='/user/new_password/' + password_reset_token,
            body={'new_password': 'new_password'}
        )
        self.assert_response_ok_and_has_message(response)
        response = self.request_login(self.app_test, user, 'new_password')
        assert response.status_code == 200

    def test_that_an_existing_user_who_has_not_reset_password_can_not_set_a_new_one(self):
        self.create_user()
        response = self.app_test.post_json(
            url='/user/new_password/' + 'foobaz',
            body={'new_password': 'new_password'}
        )
        assert response.status_code == 400
        assert 'message' in json.loads(response.data)
