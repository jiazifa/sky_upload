# -*- coding: utf-8 -*-

from typing import Any, List, Tuple
from flask import Flask, Blueprint
from config import configObj

__all__ = ['create_app', 'fetch_route']


def regist_blueprint(app: Flask):
    from app.view import api as upload_api
    app.register_blueprint(upload_api, url_prefix="/")


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(configObj)
    regist_blueprint(app)
    return app