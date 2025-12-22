from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object(config)  # Importing the config file for use by the flask server.
db = SQLAlchemy(app)

from app import routes, models