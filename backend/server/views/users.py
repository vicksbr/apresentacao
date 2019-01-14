from flask import Blueprint, render_template, jsonify, request
from server.models.user import User
import json


def create_users_blueprint(debug):
    blueprint = Blueprint("users_blueprint", __name__)

    @blueprint.route("/")
    def listusers():
        users = User.objects.all()
        if users:
            response = jsonify({
                'users':
                {user.name: user.to_dict()
                 for user in users}
            })
            httpcode = 200
        else:
            response = jsonify({'users': 'users not found'})
            httpcode = 202

        return response, httpcode

    @blueprint.route('/add', methods=['GET', 'POST'])
    def add():
        if request.method == "POST":
            data = request.get_json()
            if not data:
                response = "Invalido"
                httpcode = 400
                return json.dumps(response), httpcode

            print(data)
            name = data["name"]
            email = data["email"]
            new_user = User(name, email)
            new_user.save()
            httpcode = 201
            response = new_user.to_dict()
            return json.dumps(response), httpcode

    @blueprint.route('/showusers')
    def exemplo_users():
        users = User.objects.all()
        array = []
        if users:
            for x in users:
                print(x)
                array.append(x.name)
        return render_template("exemplo_objetos.html", objetos=array)

    return blueprint
