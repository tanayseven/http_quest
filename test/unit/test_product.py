from datetime import datetime, timedelta

import pytest

from http_quest.product_quiz.problem_statements import name_with_categories, ProductCollection, Product, ProductFactory
from test.fakes import FakeRandom, FakeDatetime


class TestProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.product_list = [
            Product('Mobile Phone', 'Electronics', 3000, datetime(2018, 2, 9), datetime(2018, 2, 11)),
            Product('Laptop', 'Electronics', 10000, datetime(2018, 4, 9), datetime(2018, 4, 11)),
            Product('Rice', 'Food', 200, datetime(2018, 2, 8), datetime(2018, 2, 13)),
            Product('Pasta', 'Food', 100, datetime(2018, 4, 17), datetime(2018, 5, 13)),
        ]
        FakeDatetime.set_next_dattime(datetime(2018, 2, 10))

    def test_product_returns_the_correct_count_for_the_solution_1(self):
        assert Product.solution_count(self.product_list) == {'count': 4}

    def test_product_returns_the_correct_count_for_the_solution_2(self):
        assert Product.solution_active_count(self.product_list) == {'count': 2}

    def test_product_returns_the_correct_count_for_the_solution_3(self):
        assert Product.solution_active_date_count_categories(self.product_list) == {'Electronics': 1, 'Food': 1}

    def test_product_returns_the_correct_count_for_the_solution_4(self):
        assert Product.solution_total_value_for_active_date(self.product_list) == {'total_value': 3200}


class TestProductCollection:
    @pytest.fixture(autouse=True)
    def setup(self):
        FakeRandom.reset()
        self.product_factory = ProductFactory()
        self.datetime_now = datetime(year=2018, month=2, day=13)

    def test_product_is_generated_correctly(self):
        self.add_one_product_to_fakers()
        product = self.product_factory.new_product(0)
        assert product.price == 300
        assert product.start_date == datetime(year=2018, month=2, day=10)
        assert product.end_date == datetime(year=2018, month=2, day=15)
        selected_key = list(name_with_categories.keys())[0]
        assert product.name == selected_key
        assert product.category == name_with_categories[selected_key]

    def test_product_collection_is_generated_correctly(self):
        self.add_three_products_to_fakers()
        products = ProductCollection.generate_products(3)
        assert len(products) == 3
        self.setup_current_product1()
        self.assert_product(products, self.id)
        self.setup_current_product2()
        self.assert_product(products, self.id)
        self.setup_current_product3()
        self.assert_product(products, self.id)

    def setup_current_product1(self):
        self.id = 0
        self.price = 300
        self.start_date_delta = 3
        self.end_date_delta = 2

    def setup_current_product2(self):
        self.id = 1
        self.price = 500
        self.start_date_delta = 1
        self.end_date_delta = 7

    def setup_current_product3(self):
        self.id = 2
        self.price = 700
        self.start_date_delta = 4
        self.end_date_delta = 2

    def add_one_product_to_fakers(self):
        self.setup_current_product1()
        self.add_product_parameters_to_fakers()

    def add_three_products_to_fakers(self):
        self.add_one_product_to_fakers()
        self.setup_current_product2()
        self.add_product_parameters_to_fakers()
        self.setup_current_product3()
        self.add_product_parameters_to_fakers()

    def add_product_parameters_to_fakers(self):
        FakeRandom.append_next_randrange([self.price, self.start_date_delta, self.end_date_delta])
        FakeDatetime.set_next_dattime(self.datetime_now)

    def assert_product(self, products, id_):
        product = products[id_]
        assert product.price == self.price
        assert product.start_date == self.datetime_now - timedelta(self.start_date_delta)
        assert product.end_date == self.datetime_now + timedelta(self.end_date_delta)
        selected_key = list(name_with_categories.keys())[id_]
        assert product.name == selected_key
        assert product.category == name_with_categories[selected_key]
