from sqlalchemy import Column, Integer, String

from rest_test.extensions import Base


class User(Base):
    __tablename__ = 'base'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
