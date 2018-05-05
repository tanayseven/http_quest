import os
import pytest
from flask.testing import FlaskClient

from rest_test.app import app
from rest_test.extensions import db


class DatabaseTest:
    @pytest.fixture(autouse=True)
    def database_setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI')
        self.client = app.test_client()
        self._ctx = app.test_request_context()
        self._ctx.push()
        db.session.remove()
        db.drop_all()
        db.create_all()
        yield
        if hasattr(self, '_ctx'):
            self._ctx.pop()


class ApiTestBase(DatabaseTest):
    @staticmethod
    def create_app() -> FlaskClient:
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        with app.app_context():
            return app.test_client()

    @pytest.fixture(autouse=True)
    def api_setup(self):
        self.app_test = self.create_app()
