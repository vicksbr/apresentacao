from mongoengine import connect


def init_db(app, config):
    connection = connect(**config["DB"])
    return connection
