"""
Application factor for flask application. Configuration class
is imported from config.py using app.config.from_object().
Extensions and route blueprints are then initialized.
Blueprints are used since app object is created at run
time and app.route() is no longer a global function
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import config

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
