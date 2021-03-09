from flask import Flask , jsonify , request
import json

#create a new app constructor
app = Flask(__name__)

#boilerplate

@app.route("/")
def index():
    return "Hello world!"

@app.route("/messages", methods=['GET'])
def get_messages():
    count = request.args.get("count")
    count2 = int(count) * -1
    with open('data.json' , 'r') as data:
        f = json.load(data)
        return jsonify({'messages' : f['messages'][count2:]})

app.run(host='0.0.0.0')


