import datetime
from typing import Union


class FakeDatetime:
    _datetime = []

    @staticmethod
    def append_next_datetime(date_value: Union[datetime.datetime, list]):
        if type(date_value) is datetime.datetime:
            FakeDatetime._datetime.append(date_value)
        elif type(date_value) is list:
            FakeDatetime._datetime.extend(date_value)

    @staticmethod
    def now():
        if len(FakeDatetime._datetime) == 1:
            return FakeDatetime._datetime[0]
        return FakeDatetime._datetime.pop(0)


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