from rest_test.extensions import app
from rest_test.products.view import products_view
from rest_test.view import root_view

app.register_blueprint(products_view)
app.register_blueprint(root_view)
