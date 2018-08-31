from flask import Flask
# in order to use the configs we import them
from .config import DevConfig

# this will initialize the application
app = Flask(__name__)
# set up configurations
app.config.from_object(DevConfig)

from app import views
