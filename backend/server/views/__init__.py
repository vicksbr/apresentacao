from .index import create_index_blueprint
from .ola import create_ola_blueprint
from .exemplo_objetos import create_exemplo_objetos_blueprint
from flask import Flask


def register_blueprints(app, debug):

    index_blueprint = create_index_blueprint()
    ola_blueprint = create_ola_blueprint(debug)
    exemplo_objetos_blueprint = create_exemplo_objetos_blueprint(debug)
    app.register_blueprint(index_blueprint, url_prefix="/")
    app.register_blueprint(ola_blueprint, url_prefix="/ola")
    app.register_blueprint(exemplo_objetos_blueprint,
                           url_prefix="/exemplo_objetos")
    return app
