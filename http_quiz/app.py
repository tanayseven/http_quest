import click
from flask import Flask
from flask_injector import FlaskInjector

from http_quiz.config import apply_dev_config, configure, apply_test_config
from http_quiz.extensions import db, jwt, migrate, mail, bcrypt
from http_quiz.product_quiz.view import products_view
from http_quiz.quiz.view import quiz_view
from http_quiz.user.user import authenticate, identity, create_user
from http_quiz.user.view import user_view
from http_quiz.view import root_view

app: Flask = Flask(__name__.split('.')[0], template_folder='template')
test_app: Flask = Flask(__name__.split('.')[0], template_folder='template')

apply_dev_config(app)
apply_test_config(test_app)


def init_ext(app_):
    # Perform migrations on the database
    db.init_app(app_)
    migrate.init_app(app_)

    # Add handlers for Flask-JWT
    jwt.identity_handler(identity)
    jwt.authentication_handler(authenticate)
    jwt.init_app(app_)

    mail.init_app(app_)
    bcrypt.init_app(app_)

    app_.register_blueprint(products_view)
    app_.register_blueprint(user_view)
    app_.register_blueprint(root_view)
    app_.register_blueprint(quiz_view)

    FlaskInjector(app=app_, modules=[configure])


init_ext(app)
init_ext(test_app)


@app.cli.command()
@click.argument('email')
def create_new_admin(email):  # pragma: no cover
    """Creates a new admin with the given username"""
    success = create_user(email=email)
    if success:
        print('Created a new user with the email: ' + email)
        return
    print('Sorry something went wrong')
    exit(-1)
