from flask_security import SQLAlchemyUserDatastore, Security

from rest_test.extensions import app, db
from rest_test.model import User, Role
from rest_test.products.view import products_view
from rest_test.view import root_view

app.register_blueprint(products_view)
app.register_blueprint(root_view)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
