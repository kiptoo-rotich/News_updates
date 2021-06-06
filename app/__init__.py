from flask import Flask
from config import DevConfig
# from app import views, error
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

#Initializing application
app = Flask(__name__,instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing flask extension
bootstrap.init_app(app)

from app import views