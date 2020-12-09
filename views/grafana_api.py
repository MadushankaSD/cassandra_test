import random

from cassandra.cqlengine import connection
from flask import Blueprint, jsonify


grafana = Blueprint("/grafana/", __name__)
connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)


@grafana.route("/search", methods=['POST'])
def search_grafana():
    data = {"item": ["upper_25", "upper_50", "upper_75", "upper_90", "upper_95"]}
    return jsonify(data)


@grafana.route("/query", methods=['POST'])
def query_grafana():
    return jsonify([
        {
            "target": "Gnip",
            "datapoints": [
                [gen_rand_num()]
            ]
        },
        {
            "target": "Google sentiment",
            "datapoints": [
                [gen_rand_num()]
            ]
        },
        {
            "target": "Google Translate",
            "datapoints": [
                [gen_rand_num()]
            ]
        },
        {
            "target": "Twitter",
            "datapoints": [
                [gen_rand_num()]
            ]
        }
    ])


@grafana.route("/annotation", methods=['POST'])
def annotate_grafana():
    return jsonify([
        {
            "text": "text shown in body",
            "title": "Annotation Title",
            "isRegion": True,
            "time": "timestamp",
            "timeEnd": "timestamp",
            "tags": ["tag1"]
        }
    ])


def gen_rand_num():
   return random.randrange(30,1000)