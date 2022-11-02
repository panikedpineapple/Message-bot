from flask import Flask , jsonify , request
import json
import dbmanager

#create a new app constructor
import settings

app = Flask(__name__)

#boilerplate

@app.route("/")
def index():
    return "Hello world!"

@app.route("/messages", methods=['GET'])
def get_messages():
    count = request.args.get("count")

    db = dbmanager.DBManager(settings.database)
    data = db.get_message_by_count(int(count))
    return jsonify(data)

@app.route("/search", methods=['GET'])
def get_messages_by_id():
    id = request.args.get("id")

    db = dbmanager.DBManager(settings.database)
    data = db.get_message_by_id(int(id))
    return jsonify(data)

app.run(host='0.0.0.0', port=80)


