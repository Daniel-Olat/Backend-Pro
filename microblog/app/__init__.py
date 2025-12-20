from flask import Config, Flask 
from config import config
app = Flask(__name__)
app.config.from_object(config) #Importing the config file for use by the flask server.
from app import routes