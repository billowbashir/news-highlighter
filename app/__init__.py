from flask import Flask
# in order to use the configs we import them
from .config import DevConfig

# this will initialize the application
app = Flask(__name__,instance_relative_config = True)
# set up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
