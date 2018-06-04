import os

from flask import Flask
from flask_bcrypt import Bcrypt
from injector import Module, provider, singleton, Binder, Injector


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
