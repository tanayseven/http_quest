import os
from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security

from rest_test.extensions import db, jwt, migrate
from rest_test.model import User, Role
from rest_test.repo import UserRepo
from rest_test.products.view import products_view
from rest_test.view import root_view

app: Flask = Flask(__name__.split('.')[0])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db.init_app(app)
migrate.init_app(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
jwt.identity_handler(UserRepo.identity)
jwt.authentication_handler(UserRepo.authenticate)
jwt.init_app(app)

app.register_blueprint(products_view)
app.register_blueprint(root_view)

