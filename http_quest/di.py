import datetime
import os
import random

from flask_bcrypt import Bcrypt
from tinydic import Container

from test.fakes import FakeBcrypt, FakeDatetime, FakeRandom
from http_quest.ext import bcrypt
from http_quest.utilities import RandomWrapper


container = Container()


def bind_injections_test():
    container.bcrypt = FakeBcrypt()
    container.datetime = FakeDatetime()
    container.random = FakeRandom()


def bind_injections_dev():  # pragma: no cover
    container.bcrypt = bcrypt
    container.datetime = datetime.datetime
    container.random = random


if os.environ['APP_ENVIRONMENT'] == 'dev':  # pragma: no cover
    bind_injections_dev()
elif os.environ['APP_ENVIRONMENT'] == 'test':
    bind_injections_test()