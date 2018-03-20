import pytest
from flask.testing import FlaskClient
from flask_testing import LiveServerTestCase

from http_endpoints_test.mock_server import app


class ApiTestBase(LiveServerTestCase):
    def create_app(self) -> FlaskClient:
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        return app

