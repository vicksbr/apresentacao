from flask import Blueprint, render_template


def create_ola_blueprint(debug):
    blueprint = Blueprint("ola_blueprint", __name__)

    @blueprint.route("/")
    @blueprint.route("/<string:name>")
    def ola(name=None):
        if not name:
            return render_template("ola.html", debug=debug)
        return render_template("ola.html", name=name, debug=debug)

    return blueprint
