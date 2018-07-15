import datetime
import random
import os

from flask import Flask, g
from flask_bcrypt import Bcrypt

from http_quiz.utilities import RandomWrapper
from http_quiz.ext import bcrypt
from test.fakes import FakeDatetime, FakeRandom, FakeBcrypt


def bind_injections_test(app: Flask):
    with app.app_context():
        g.bcrypt = FakeBcrypt()
        g.datetime = FakeDatetime()
        g.random = FakeRandom()


def bind_injections_dev(app: Flask):  # pragma: no cover
    with app.app_context():
        g.bcrypt = bcrypt
        g.datetime = datetime.datetime
        g.random = random
