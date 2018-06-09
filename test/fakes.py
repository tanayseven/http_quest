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