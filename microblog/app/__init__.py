from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

app = Flask(__name__)
app.config.from_object(config)  # Importing the config file for use by the flask server.
db = SQLAlchemy(app)
# Initialize Flask-Migrate so the flask CLI can access migration commands
migrate = Migrate(app, db)

from app import routes, models