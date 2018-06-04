import os

from flask import Flask
from flask_bcrypt import Bcrypt
from injector import singleton, Module, provider, Binder, Injector


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOCALE = os.environ.get('APP_LOCALE')
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_PASSWORD_KEY = 'password'
    JWT_AUTH_URL_RULE = '/user/login'
    MAIL_DEFAULT_SENDER = 'noreply@resttest.com'


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    MAIL_SERVER = 'mailcatcher'
    MAIL_PORT = '1025'
    MAIL_SUPPRESS_SEND = False


class TestConfig(Config):
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    FLASK_DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret'
    MAIL_SUPPRESS_SEND = True


class FakeDatetime:
    _datetime = None

    @staticmethod
    def set_current_datetime(datetime_now):
        FakeDatetime._datetime = datetime_now

    @staticmethod
    def now():
        return FakeDatetime._datetime


class FakeRandom:
    _randrange = []

    @staticmethod
    def set_randrange(rand_range: list = None):
        if rand_range is None:
            rand_range = []
        FakeRandom._randrange = rand_range

    @staticmethod
    def randrange():
        return FakeRandom._randrange


class FakeBcrypt:
    def generate_password_hash(self, x, **kwargs):
        return x.encode()

    def check_password_hash(self, x, y):
        return x == y


class DevInjectionsModule(Module):
    @provider
    @singleton
    def provide_bcrypt(self, app: Flask) -> Bcrypt:
        return Bcrypt(app)


def bind_injections_test(binder: Binder):
    binder.bind(
        Bcrypt,
        to=FakeBcrypt(),
        scope=singleton,
    )


injector: Injector = None
if os.environ['APP_ENVIRONMENT'] == 'dev':
    injector = Injector([DevInjectionsModule])
elif os.environ['APP_ENVIRONMENT'] == 'test':
    injector = Injector([bind_injections_test])
