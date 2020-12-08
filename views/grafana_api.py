from cassandra.cqlengine import connection
from flask import Blueprint, jsonify

grafana = Blueprint("/grafana/", __name__)
connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)


@grafana.route("/search", methods=['POST'])
def search_grafana():
    return jsonify(["upper_25", "upper_50", "upper_75", "upper_90", "upper_95"])


@grafana.route("/query", methods=['POST'])
def query_grafana():
    return jsonify([
        {
            "target": "pps in",
            "datapoints": [
                [622, 1450754160000],
                [365, 1450754220000]
            ]
        },
        {
            "target": "pps out",
            "datapoints": [
                [861, 1450754160000],
                [767, 1450754220000]
            ]
        },
        {
            "target": "errors out",
            "datapoints": [
                [861, 1450754160000],
                [767, 1450754220000]
            ]
        },
        {
            "target": "errors in",
            "datapoints": [
                [861, 1450754160000],
                [767, 1450754220000]
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
