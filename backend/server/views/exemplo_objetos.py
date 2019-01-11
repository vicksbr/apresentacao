from flask import Blueprint, render_template


def create_exemplo_objetos_blueprint(debug):

    arr_objetos = ['laranja', 'pera', 'uva']
    blueprint = Blueprint("exemplo_objetos_blueprint", __name__)

    @blueprint.route('/')
    def exemplo_objetos():
        return render_template("exemplo_objetos.html", objetos=arr_objetos)

    return blueprint
