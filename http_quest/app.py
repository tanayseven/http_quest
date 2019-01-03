import os

from flask import Flask

from http_quest.ext import bcrypt, db, jwt, mail, migrate
from http_quest.product_quiz.view import products_view
from http_quest.quiz.view import quiz_view
from http_quest.user.user import authenticate, identity
from http_quest.user.view import user_view
from http_quest.view import root_view

app: Flask = Flask(__name__.split('.')[0], template_folder='template')

if os.environ['APP_ENVIRONMENT'] in ('dev', 'prod',):  # pragma: no cover
    app.config.from_object('http_quest.config.DevelopmentConfig')
elif os.environ['APP_ENVIRONMENT'] in ('test',):
    app.config.from_object('http_quest.config.TestConfig')

# Perform migrations on the data
db.init_app(app)
migrate.init_app(app)

# Add handlers for Flask-JWT
jwt.identity_handler(identity)
jwt.authentication_handler(authenticate)
jwt.init_app(app)

mail.init_app(app)

bcrypt.init_app(app)

app.register_blueprint(products_view)
app.register_blueprint(user_view)
app.register_blueprint(root_view)
app.register_blueprint(quiz_view)

if __name__ == "__main__":
    app.run()
