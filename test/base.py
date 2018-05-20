import os
import re

import pytest
from flask import json
from flask.testing import FlaskClient
from types import MethodType

from http_quiz.app import app
from http_quiz.extensions import db, mail, bcrypt
from http_quiz.user.model import User
from http_quiz.user.repo import UserRepo
from http_quiz.user.user import create_user


def _post_json(self, url: str = '/', body=None, headers=None):
    headers = {} if headers is None else headers
    body = {} if body is None else body
    return self.post(
        url,
        data=json.dumps(body),
        content_type='application/json',
        headers=headers,
    )


class DatabaseTest:
    @staticmethod
    def new_user(email: str=None, password: str=None):
        return User(
            email=email or 'user@domain.com',
            password=bcrypt.generate_password_hash(password or 'password').decode(),
        )

    @pytest.fixture(autouse=True)
    def database_setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI')
        self._ctx = app.test_request_context()
        self._ctx.push()
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield
        if hasattr(self, '_ctx'):
            self._ctx.pop()


class ApiTestBase(DatabaseTest):
    def create_user(self):
        create_user('user@domain.com', 'password')
        self.mail_outbox.pop()
        return UserRepo.fetch_user_by_email('user@domain.com')

    @staticmethod
    def create_app() -> FlaskClient:
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['MAIL_SUPPRESS_SEND'] = True
        mail.init_app(app)
        with app.app_context():
            return app.test_client()

    @pytest.fixture
    def mail_outbox(self):
        with mail.record_messages() as outbox:
            yield outbox

    @pytest.fixture(autouse=True)
    def api_setup(self, mail_outbox):
        self.app_test = self.create_app()
        self.mail_outbox = mail_outbox
        if os.environ.get('FAST_TESTS'):
            bcrypt.generate_password_hash = lambda x: x.encode()
            bcrypt.check_password_hash = lambda x, y: x == y
        self.app_test.post()
        self.app_test.post_json = MethodType(_post_json, self.app_test)

    @staticmethod
    def request_login(app_test, user: User, password: str = None):
        request_payload = {'email': user.email, 'password': 'password' if password is None else password}
        response = app_test.post_json(url='/user/login', body=request_payload)
        return response

    @staticmethod
    def request_login_token(app_test, user: User) -> str:
        response = ApiTestBase.request_login(app_test, user)
        token = 'JWT ' + json.loads(response.data)['access_token']
        return token

    @staticmethod
    def assert_response_ok_and_has_message(response):
        assert response.status_code == 200
        assert 'message' in json.loads(response.data)

    def mail_body_json(self) -> dict:
        return json.loads(self.mail_outbox[0].body.replace("'", '"'))

    def mail_body_extract_token(self) -> str:
        uuid_pattern = re.compile(r'([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})')
        match = uuid_pattern.search(self.mail_outbox[0].body)
        return match.string[match.start():match.end()]

    def assert_has_one_mail_with_subject(self, subject):
        assert len(self.mail_outbox) == 1
        assert self.mail_outbox[0].subject == subject

    def assert_has_one_mail_with_subject_and_recipients(self, subject, recipients):
        self.assert_has_one_mail_with_subject(subject)
        assert set(self.mail_outbox[0].recipients) == set(recipients)

