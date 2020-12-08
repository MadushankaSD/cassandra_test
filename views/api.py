from cassandra.cqlengine import connection
from flask import Blueprint, request
from model.Person import Person
from flask import jsonify

api = Blueprint("api", __name__)
connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)


@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return jsonify("HELLO")


@api.route("/add", methods=['POST'])
def add_person():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    person = Person.create(first_name=first_name, last_name=last_name)
    person.save()
    return jsonify(person.get_data())


@api.route("/sdas", methods=['POST'])
def get_all():
    persons = Person.objects().all()
    return jsonify([person.get_data() for person in persons])


# @api.route("/query", methods=['POST'])
# def get_all():
#     persons = Person.objects().all()
#     return jsonify([person.get_data() for person in persons])


@api.route("/delete", methods=["DELETE"])
def delete():
    id = request.form["id"]
    person = Person.objects().get(id=id)
    person.delete()
    return "Done"


@api.route("/update", methods=["PUT"])
def update():
    id = request.form["id"]
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    person = Person.objects().get(id=id)
    person.update(first_name=first_name, last_name=last_name)
    person.save()
    return "success"
