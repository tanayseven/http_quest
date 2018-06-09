from datetime import datetime

import pytest

from http_quiz.di import injector
from http_quiz.product_quiz.problem_statements import ProductFactory, name_with_categories
from test.fakes import FakeRandom, FakeDatetime


class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.price = 300
        self.start_date_delta = 3
        self.end_date_delta = 2
        self.datetime_now = datetime(year=2018, month=2, day=13)
        FakeRandom.set_randrange([self.price, self.start_date_delta, self.end_date_delta])
        FakeDatetime.set_current_datetime(datetime_now=self.datetime_now)
        self.product_factory: ProductFactory = injector.get(ProductFactory)

    def test_product_is_generated_correctly(self):
        product = self.product_factory.new_product(0)
        assert product.price == 300
        assert product.start_date == datetime(year=2018, month=2, day=10)
        assert product.end_date == datetime(year=2018, month=2, day=15)
        selected_key = list(name_with_categories.keys())[0]
        assert product.name == selected_key
        assert product.category == name_with_categories[selected_key]

    def test_product_collection_is_generated_correctly(self):
        pass
