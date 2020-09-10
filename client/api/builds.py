import json
import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_caching import Cache
from flask_cors import CORS

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable caching
app.config.from_mapping(config)
cache = Cache(app)

# enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

with open('api/builds.json') as file7:
    builds = json.load(file7)
with open('api/stats.json') as file8:
    stats = json.load(file8)

response_object = {'status': 'success', 'message':''}
@app.route('/api/builds', methods=['GET'])
def get_builds():
    response_object['message'] = 'Got the builds/stats!'
    response_object['builds'] = builds
    response_object['stats'] = stats
    # response_object['champs'] = champList
    return jsonify(response_object)
