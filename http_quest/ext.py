from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
jwt = JWT()
migrate: Migrate = Migrate(db=db)
mail: Mail = Mail()
bcrypt: Bcrypt = Bcrypt()
babel: Babel = Babel()
