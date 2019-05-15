import os
import random

import datetime

from http_quest.container import Container
from http_quest.ext import bcrypt
from test.fakes import FakeBcrypt, FakeDatetime, FakeRandom

container = Container()


def bind_injections_test():
    container.bcrypt = FakeBcrypt()
    container.datetime = FakeDatetime()
    container.random = FakeRandom()


def bind_injections_dev():  # pragma: no cover
    container.bcrypt = bcrypt
    container.datetime = datetime.datetime
    container.random = random


if os.environ['APP_ENVIRONMENT'] in ('dev', 'prod',):  # pragma: no cover
    bind_injections_dev()
elif os.environ['APP_ENVIRONMENT'] in ('test',):
    bind_injections_test()
