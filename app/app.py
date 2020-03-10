from flask import Flask
from .config import Config
from . import view

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    view.init_app(app)
    return app