from flask import Flask

from rest_test.products.view import products_view
from rest_test.view import root_view

app = Flask(__name__)

app.register_blueprint(products_view)
app.register_blueprint(root_view)
