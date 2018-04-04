import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Base = declarative_base()

engine = create_engine(os.environ.get('DATABASE_URL'))

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

