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
    _count = 0

    @staticmethod
    def set_randrange(rand_range: list = None):
        if rand_range is None:
            rand_range = []
        FakeRandom._count = 0
        FakeRandom._randrange = rand_range

    @staticmethod
    def randrange(*args, **kwargs):
        FakeRandom._count += 1
        return FakeRandom._randrange[FakeRandom._count - 1]


class FakeBcrypt:
    def generate_password_hash(self, x, **kwargs):
        return x.encode()

    def check_password_hash(self, x, y):
        return x == y