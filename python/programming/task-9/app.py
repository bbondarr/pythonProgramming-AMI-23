import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from config import USERNAME, PASSWORD

# Initalizing API
app = Flask(__name__)

# Creating and setting up database
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@localhost:5432/products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

