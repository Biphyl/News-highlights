from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig


def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(cofig_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

from .main import views