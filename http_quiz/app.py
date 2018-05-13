import os
from flask import Flask

from http_quiz.config import apply_dev_config
from http_quiz.extensions import db, jwt, migrate, mail, bcrypt
from http_quiz.product.view import products_view
from http_quiz.quiz.view import quiz_view
from http_quiz.user.user import authenticate, identity
from http_quiz.user.view import user_view
from http_quiz.view import root_view

app: Flask = Flask(__name__.split('.')[0])

if os.environ.get('APP_ENVIRONMENT').lower() == 'dev':
    apply_dev_config(app)

# Perform migrations on the database
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
