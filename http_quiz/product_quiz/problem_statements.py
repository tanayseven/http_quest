import datetime
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


class Product:
    name: str = ''
    category: str = ''
    price: int = 0
    start_date: datetime.datetime = None
    end_date: datetime.datetime = None

    @inject
    def __init__(self, id_: int=0, random: RandomWrapper=RandomWrapper()):
        self.name = list(name_with_categories.keys())[id_]
        self.category = name_with_categories[self.name]
        self.price = random.randrange(100, 10000)
        # start_date = datetime.datetime.now() - datetime.timedelta.days


class ProductCollection:
    def __init__(self, count: int):
        self._products = self.generate_products(count)

    @staticmethod
    def generate_products(count: int) -> List[Product]:
        return [
            Product(x) for x in range(count)
        ]
