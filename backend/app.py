from flask import Flask
from server import create_app

debug = __name__ == '__main__'

app = create_app(debug)


if __name__ == '__main__':
    app.run()
