from flask import Flask, Blueprint, render_template
from .views import register_blueprints
from .database import init_db
from .config import config


def create_app(debug):
    app = Flask(__name__)
    app = register_blueprints(app, debug)
    connection = init_db(app, config)

    return app
