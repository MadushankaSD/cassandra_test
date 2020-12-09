from cassandra.cluster import Cluster
from flask import Flask
from views.api import api
from flask_cors import CORS
from views.grafana_api import grafana
from script import sync_db

KEYSPACE = 'test'


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(api)
    app.register_blueprint(grafana)
    # app.debug = True
    cluster = Cluster()
    # cluster = Cluster(['',''])
    session = cluster.connect()
    session.execute(
        """CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };""" % KEYSPACE)
    cluster.connect(keyspace=KEYSPACE)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
