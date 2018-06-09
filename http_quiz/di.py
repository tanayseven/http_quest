import datetime
import os

from flask_bcrypt import Bcrypt
from injector import singleton, Binder, Injector

from http_quiz.utilities import RandomWrapper
from test.fakes import FakeDatetime, FakeRandom, FakeBcrypt


def bind_injections_test(binder: Binder):
    binder.bind(
        Bcrypt,
        to=FakeBcrypt(),
        scope=singleton,
    )
    binder.bind(
        datetime.datetime,
        to=FakeDatetime(),
        scope=singleton,
    )
    binder.bind(
        RandomWrapper,
        to=FakeRandom(),
        scope=singleton,
    )


def bind_injections_dev(binder: Binder):
    pass


injector: Injector = None
if os.environ['APP_ENVIRONMENT'] == 'test':
    injector = Injector([bind_injections_test])
elif os.environ['APP_ENVIRONMENT'] == 'dev':
    injector = Injector([bind_injections_dev])
