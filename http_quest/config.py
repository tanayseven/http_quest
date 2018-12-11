import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOCALE = os.environ.get('APP_LOCALE')
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_PASSWORD_KEY = 'password'
    JWT_AUTH_URL_RULE = '/user/login'
    SECRET_KEY = 'secret'
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
    MAIL_SUPPRESS_SEND = True
