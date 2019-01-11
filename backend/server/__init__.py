from flask import Flask, Blueprint, render_template
from .views import register_blueprints


def create_app(debug):
    app = Flask(__name__)
    app = register_blueprints(app, debug)
    app.secret_key = "dev"

    return app
