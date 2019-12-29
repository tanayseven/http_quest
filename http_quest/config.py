import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI',
        'postgresql://http_quest:http_quest@localhost:5432/http_quest_test'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOCALE = os.environ.get('APP_LOCALE', 'en')
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_PASSWORD_KEY = 'password'
    JWT_AUTH_URL_RULE = '/user/login'
    SECRET_KEY = 'secret'
    MAIL_DEFAULT_SENDER = 'noreply@resttest.com'
    SUPPORTED_LANGUAGES = {'hi': 'Hindi', 'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    MAIL_SERVER = 'mailcatcher'
    MAIL_PORT = '1025'
    MAIL_SUPPRESS_SEND = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URI',
        'postgresql://http_quest:http_quest@localhost:5432/http_quest_test',
    )
    FLASK_DEBUG = True
    TESTING = True
    MAIL_SUPPRESS_SEND = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI',
        'postgresql://http_quest:http_quest@localhost:5432/http_quest_test',
    )
    FLASK_DEBUG = False
    TESTING = False
    MAIL_SERVER = 'mailcatcher'
    MAIL_PORT = '1025'
    MAIL_SUPPRESS_SEND = False


CONFIG = {
    'test': TestConfig,
    'dev': DevelopmentConfig,
    'prod': ProdConfig,
}[os.environ.get('APP_ENVIRONMENT', 'test')]
