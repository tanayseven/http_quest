from http_quest.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(64))
    active = db.Column(db.Boolean())
    password_reset_token = db.Column(db.String(255), unique=True, nullable=True)
