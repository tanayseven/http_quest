import datetime
from copy import deepcopy
from datetime import timedelta
from typing import List

from injector import inject

from http_quiz.di import injector
from http_quiz.utilities import RandomWrapper

name_with_categories = {
    'Mobile Phone': 'Electronics',
    'Laptop': 'Electronics',
    'Charger': 'Electronics',
    'Rice': 'Food',
    'Wheat': 'Food',
    'Pulses': 'Food',
    'Milk': 'Food',
    'Shirt': 'Outfit',
    'Pants': 'Outfit',
    'T-Shirt': 'Outfit',
    'Skirt': 'Outfit',
    'Fight \'em': 'Gaming',
    'Race \'em': 'Gaming',
}


class Product:
    def __init__(
            self,
            name: str,
            category: str,
            price: int,
            start_date: datetime.datetime,
            end_date: datetime.datetime,
    ):
        self.name = name
        self.category = category
        self.price = price
        self.start_date = start_date
        self.end_date = end_date


class ProductFactory:
    @inject
    def __init__(self, random: RandomWrapper = RandomWrapper(), datetime: datetime.datetime = datetime.datetime):
        self._random = random
        self._datetime = datetime

    def new_product(self, id_: int):
        name = list(name_with_categories.keys())[id_]
        return Product(
            name,
            name_with_categories[name],
            self._random.randrange(100, 10000),
            self._datetime.now() - timedelta(days=self._random.randrange(2, 9)),
            self._datetime.now() + timedelta(days=self._random.randrange(2, 9)),
        )


product_factory = injector.get(ProductFactory)


class ProductCollection:
    @staticmethod
    def generate_products(count: int) -> List[Product]:
        return [
            product_factory.new_product(x) for x in range(count)
        ]
