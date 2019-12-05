import datetime
from typing import Union


class FakeDatetime:
    _datetime: datetime.datetime

    @staticmethod
    def set_next_dattime(date_value: datetime.datetime):
        FakeDatetime._datetime = date_value

    @staticmethod
    def now():
        return FakeDatetime._datetime


class FakeRandom:
    _rand_range = []

    @staticmethod
    def append_next_randrange(rand_range: Union[list, int] = 0):
        if type(rand_range) is int:
            FakeRandom._rand_range.append(rand_range)
        elif type(rand_range) is list:
            FakeRandom._rand_range.extend(rand_range)

    @staticmethod
    def reset():
        FakeRandom._rand_range = []

    @staticmethod
    def randrange(*args, **kwargs):
        return FakeRandom._rand_range.pop(0)


class FakeBcrypt:
    def generate_password_hash(self, x, **kwargs):
        return x.encode()

    def check_password_hash(self, x, y):
        return x == y