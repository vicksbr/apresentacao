
from flask import Blueprint, render_template


def create_index_blueprint():
    blueprint = Blueprint("index_blueprint", __name__)

    @blueprint.route("/")
    def index():
        return render_template("index.html")

    return blueprint
