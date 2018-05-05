import os
from flask import Flask

from rest_test.extensions import db, jwt, migrate
from rest_test.product.view import products_view
from rest_test.repo import UserRepo
from rest_test.view import root_view

app: Flask = Flask(__name__.split('.')[0])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'
app.config['JWT_AUTH_URL_RULE'] = '/login'

db.init_app(app)
migrate.init_app(app)
jwt.identity_handler(UserRepo.identity)
jwt.authentication_handler(UserRepo.authenticate)
jwt.init_app(app)

app.register_blueprint(products_view)
app.register_blueprint(root_view)

