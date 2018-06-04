from flask_jwt import JWT
from flask_mail import Mail
from flask_migrate import Migrate

from http_quiz.ext import db

jwt = JWT()
migrate: Migrate = Migrate(db=db)
mail: Mail = Mail()
