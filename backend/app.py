from flask import Flask
import pprint

app = Flask(__name__)

debug = app.config['DEBUG']
debug = __name__ == '__main__'
name = __name__


@app.route("/")
def index():
    print(app.debug)
    print(f'print na rota com debug={app.debug}')
    return "Hello World!"


@app.route("/ola")
def minharota():
    print('print na rota ola')
    return "Hello World minharota!"


@app.route("/ola/<string:name>")
def hello_custom_name(name):
    content = "Ola meu amigosssss: " + str(name)
    return content


variables_and_printmsgs = [
    (app.__dir__, 'print no debug'),
    (app.config, 'Printando as app.config para mostrar as defaults configs'),
    (app.blueprints, 'Printando as app.blueprints'),
    (app.static_folder, 'Printando o app.static_folder'),
    (app.template_folder, "Printando o app.template_folder"),
    (app.instance_path, 'Printando o app.instance_path'),
    (app.debug, 'Printando o debug'),
]


def printDebugs(debugs_array_of_tuples):
    for item in debugs_array_of_tuples:
        pp = pprint.PrettyPrinter(indent=4)
        print(item[1])
        pp.pprint(item[0])
        print('\n')


if __name__ == '__main__':
    printDebugs(variables_and_printmsgs)
    app.run(debug=debug)
