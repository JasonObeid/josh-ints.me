import csv
import datetime
import json
import operator
import random
import sys
import time
from collections import Counter
from math import floor
from statistics import mean, mode

import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_caching import Cache
from flask_cors import Compress
from utils.helperFunctions import *

# starting summoners
global SUMMONERS
SUMMONERS = [
    {
        'id': '',
        'summId': '',
        'name': 'MundoLikey',
        'history': [],
        'startIndex': 0,
        'endIndex': 10,
        'matchInfo': [],
        'rank': ''
    },
]

for summoner in SUMMONERS:
    accountId, summonerId = getIds(summoner['name'])
    history = getHistory(accountId)
    summoner['id'] = accountId
    summoner['summId'] = summonerId
    summoner['history'] = history
    summoner['matchInfo'] = getMatch(history, accountId)
    summoner['rank'] = getRank(summonerId)

summonersResponse = {'status': 'success', 'message': ''}
buildsResponse = {'status': 'success', 'message': ''}

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
# instantiate the app
app = Flask(__name__)

# enable caching
app.config.from_mapping(config)
cache = Cache(app)

# enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

# '/<path:path>') means path plus passes path as parameter
# you can have multiple routes for one method


@app.route('/api/summoners', methods=['GET', 'PUT'])
def all_summoners():
    global SUMMONERS
    if request.method == 'PUT':
        post_data = request.get_json()
        accId, summId = getIds(post_data.get('name'))
        if(accId == 'Summoner not found'):
            summonersResponse['status'] = 'failure'
            summonersResponse['message'] = accId
        else:
            history = getHistory(accId)
            if(history == 'Match history not found'):
                summonersResponse['status'] = 'failure'
                summonersResponse['message'] = history
            else:
                newSummoner = {
                    'id': accId,
                    'summId': summId,
                    'name': post_data.get('name'),
                    'history': history,
                    'matchInfo': getMatch(history, accId),
                    'startIndex': 0,
                    'endIndex': 10,
                    'rank': getRank(summId)
                }
                SUMMONERS.append(newSummoner)
                summonersResponse['message'] = 'Summoner added!'
                summonersResponse['summoners'] = newSummoner
    else:
        #summonersResponse['message'] = 'Summoner added!'
        summonersResponse['summoners'] = SUMMONERS
    return jsonify(summonersResponse)


@app.route('/api/summoners/<summoner_id>', methods=['PUT', 'DELETE'])
def single_summoner(summoner_id):
    if request.method == 'PUT':
        post_data = request.get_json()
        summonersResponse[summoner_id] = get_more_matches_summoner(
            summoner_id, post_data)
    if request.method == 'DELETE':
        remove_summoner(summoner_id)
        summonersResponse['message'] = 'Summoner removed!'
    return jsonify(summonersResponse)


@app.route('/api/refresh', methods=['PUT'])
def refresh_summoners():
    global SUMMONERS
    print(SUMMONERS)
    SUMMONERS = refreshSummoners()
    print(SUMMONERS)
    summonersResponse['message'] = 'Summoners refreshed!'
    summonersResponse['summoners'] = SUMMONERS
    return jsonify(summonersResponse)


@app.route('/api/builds', methods=['GET'])
def get_builds():
    buildsResponse['message'] = 'Got the builds/stats!'
    buildsResponse['builds'] = builds
    buildsResponse['stats'] = stats
    buildsResponse['indexMap'] = indexMap
    buildsResponse['runeMap'] = runeMap
    buildsResponse['shardMap'] = shardList
    return jsonify(buildsResponse)


@app.route('/api/update', methods=['GET'])
def refresh_builds():
    buildList, stats = getMobalytics()
    buildsResponse['message'] = 'Builds refreshed!'
    buildsResponse['builds'] = buildList
    buildsResponse['stats'] = stats
    return jsonify(buildsResponse)


@app.route('/api/test', methods=['GET'])
def test():
    with open('dataDragon/runesReforged.json') as file11:
        indexMap = json.load(file11)
        return jsonify(indexMap)


# endpoint helper functions
def remove_summoner(summoner_id):
    for summoner in SUMMONERS:
        if summoner['id'] == summoner_id:
            SUMMONERS.remove(summoner)
            return True
    return False


def get_more_matches_summoner(summoner_id, post_data):
    accId = post_data.get('id')
    startIndex = post_data.get('startIndex')
    endIndex = post_data.get('endIndex')
    history = getHistory(accId, startIndex, endIndex)
    matchInfo = getMatch(history, accId)
    for summoner in SUMMONERS:
        if summoner['id'] == summoner_id:
            summoner['history'] += history
            summoner['startIndex'] = startIndex
            summoner['endIndex'] = endIndex
            summoner['matchInfo'] += matchInfo
            return summoner
    return SUMMONERS[0]


def refreshSummoners():
    newSummoners = []
    for summoner in SUMMONERS:
        accountId = summoner['id']
        name = summoner['name']
        summonerId = summoner['summId']
        history = getHistory(accountId)
        matchInfo = getMatch(history, accountId)
        rank = getRank(summonerId)
        startIndex = summoner['startIndex']
        endIndex = len(history)
        summoner = {'id': accountId, 'name': name, 'summId': summonerId,
                    'history': history, 'matchInfo': matchInfo,
                    'startIndex': startIndex, 'endIndex': endIndex, 'rank': rank}
        newSummoners.append(summoner)
    print('I refreshed')
    print(newSummoners)
    return newSummoners


if __name__ == "__main__":
    app.run()
