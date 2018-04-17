import os
import pytest
from flask import Flask
from flask_testing import LiveServerTestCase

from rest_test.app import app
from rest_test.extensions import db


class ApiTestBase(LiveServerTestCase):
    def create_app(self) -> Flask:
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        return app


class DatabaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
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
