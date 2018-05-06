import os
from flask import Flask
from flask_injector import FlaskInjector

from rest_test.di import configure
from rest_test.extensions import db, jwt, migrate, mail
from rest_test.product.view import products_view
from rest_test.user.repo import UserRepo
from rest_test.user.view import user_view
from rest_test.view import root_view

app: Flask = Flask(__name__.split('.')[0])

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Config for SQL-Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

# Config for Flask-JWT
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'
app.config['JWT_AUTH_URL_RULE'] = '/user/login'

# Config for Flask-Mail
app.config['MAIL_SERVER'] = 'mailcatcher'
app.config['MAIL_PORT'] = '1025'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@resttest.com'

# Perform migrations on the database
db.init_app(app)
migrate.init_app(app)

# Add handlers for Flask-JWT
jwt.identity_handler(UserRepo.identity)
jwt.authentication_handler(UserRepo.authenticate)
jwt.init_app(app)

mail.init_app(app)

app.register_blueprint(products_view)
app.register_blueprint(user_view)
app.register_blueprint(root_view)

FlaskInjector(app=app, modules=[configure])
