from .index import create_index_blueprint
from .users import create_users_blueprint
from flask import Flask


def register_blueprints(app, debug):

    index_blueprint = create_index_blueprint()
    users_blueprint = create_users_blueprint(debug)

    app.register_blueprint(index_blueprint, url_prefix="/")
    app.register_blueprint(users_blueprint, url_prefix="/api/users")

    return app
