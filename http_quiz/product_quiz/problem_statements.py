import datetime
from copy import deepcopy
from datetime import timedelta
from typing import List

from injector import inject

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


class ProductFactory:
    name: str = ''
    category: str = ''
    price: int = 0
    start_date: datetime.datetime = None
    end_date: datetime.datetime = None

    @inject
    def __init__(self, random: RandomWrapper=RandomWrapper(), datetime: datetime.datetime=datetime.datetime):
        self._random = random
        self._datetime = datetime

    def new_product(self, id_: int):
        self.name = list(name_with_categories.keys())[id_]
        self.category = name_with_categories[self.name]
        self.price = self._random.randrange(100, 10000)
        self.start_date = self._datetime.now() - timedelta(days=self._random.randrange(2, 9))
        self.end_date = self._datetime.now() + timedelta(days=self._random.randrange(2, 9))
        return deepcopy(self)


class ProductCollection:
    def __init__(self, count: int):
        self._products = self.generate_products(count)

    @staticmethod
    def generate_products(count: int) -> List[ProductFactory]:
        return [
            ProductFactory(x) for x in range(count)
        ]
