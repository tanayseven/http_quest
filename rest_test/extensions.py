from flask_jwt import JWT
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


jwt = JWT()
db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate(db=db)
