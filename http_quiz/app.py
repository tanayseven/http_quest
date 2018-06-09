import os

import click
from flask import Flask

from http_quiz.ext import db
from http_quiz.extensions import jwt, migrate, mail, bcrypt
from http_quiz.product_quiz.view import products_view
from http_quiz.quiz.view import quiz_view
from http_quiz.user.user import identity, bcrypt_auth, BcryptAuth
from http_quiz.user.view import user_view
from http_quiz.view import root_view

app: Flask = Flask(__name__.split('.')[0], template_folder='template')

if os.environ['APP_ENVIRONMENT'] == 'dev':
    app.config.from_object('http_quiz.config.DevelopmentConfig')
elif os.environ['APP_ENVIRONMENT'] == 'test':
    app.config.from_object('http_quiz.config.TestConfig')

# Perform migrations on the data
db.init_app(app)
migrate.init_app(app)

# Add handlers for Flask-JWT
jwt.identity_handler(identity)
jwt.authentication_handler(bcrypt_auth.authenticate)
jwt.init_app(app)

mail.init_app(app)

bcrypt.init_app(app)

app.register_blueprint(products_view)
app.register_blueprint(user_view)
app.register_blueprint(root_view)
app.register_blueprint(quiz_view)


@app.cli.command()
@click.argument('email')
def create_new_admin(email):
    """Creates a new admin with the given username"""
    success = bcrypt_auth.create_user(email=email)
    if success:
        print('Created a new user with the email: ' + email)
        return
    print('Sorry something went wrong')
    exit(-1)
