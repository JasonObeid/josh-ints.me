
import requests
from collections import Counter
import csv
import json
from statistics import mean, mode
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

with open('./api/dataDragon/champIds.json') as file1:
    champList = json.load(file1)
with open('./api/dataDragon/branchIds.json') as file3:
    branchList = json.load(file3)
with open('./api/dataDragon/runeIds.json') as file4:
    runeList = json.load(file4)
with open('./api/dataDragon/itemIds.json') as file5:
    itemList = json.load(file5)
with open('./api/dataDragon/shardIds.json') as file6:
    shardList = json.load(file6)
with open('./api/dataDragon/summonerIds.json') as file7:
    spellList = json.load(file7)

def getSpells(spellIds):
    spells = []
    spell1 = spellList[str(spellIds[0])]
    spell2 = spellList[str(spellIds[1])]
    spells.append(spell1)
    spells.append(spell2)
    return spells

def getRunes(runeIds, style, substyle):
    runes = {}
    primary = branchList[str(style)]
    secondary = branchList[str(substyle)]
    keystoneId = str(runeIds[0])
    keystone = runeList[keystoneId]
    primary1Id = str(runeIds[1])
    primary1 = runeList[primary1Id]
    primary2Id = str(runeIds[2])
    primary2 = runeList[primary2Id]
    primary3Id = str(runeIds[3])
    primary3 = runeList[primary3Id]
    secondary0Id = str(runeIds[4])
    secondary0 = runeList[secondary0Id]
    secondary1Id = str(runeIds[5])
    secondary1 = runeList[secondary1Id]
    primaryBranch = {'keystone': keystone, 'perk1': primary1, 'perk2': primary2, 'perk3': primary3,
                    'name': primary['name'], 'imgPath': primary['imgPath']}
    secondaryBranch = {'perk0': secondary0, 'perk1': secondary1,
                    'name': secondary['name'], 'imgPath': secondary['imgPath']}
    auxillary = [shardList[str(runeIds[6])], shardList[str(runeIds[7])], shardList[str(runeIds[8])]]

    runes['primaryBranch'] = primaryBranch
    runes['secondaryBranch'] = secondaryBranch
    runes['auxillary'] = auxillary
    return runes

def getItemsTrinket(itemIds, trinketId):
    items = {}
    itemsList = []
    if trinketId != 0:
        trinketName = itemList[str(trinketId)]
    else:
        trinketName = ''
    for item in itemIds:
        if(item != 0):
            name = itemList[str(item)]
            itemsList.append(name)
    items['itemsList'] = itemsList
    items['count'] = len(itemsList)  # not including trinket
    items['trinket'] = trinketName
    return items

def getItems(itemIds):
    itemsList = []
    print(itemIds)
    for item in itemIds:
        if(item != 0):
            name = itemList[str(item)]
            itemsList.append(name)
    return itemsList

def getSkills(order, customSkills):
    skills = []
    skillMap = {'Q':1, 'W':2, 'E':3}
    for skill in order:
        skillIndex = skillMap[skill]
        name = customSkills[skillIndex]['name']
        imgPath = 'images/spell/' + customSkills[skillIndex]['image'] + '.jpg'
        skills.append({'name':name, 'imgPath':imgPath, 'button':skill})
    return skills

def cleanStats(body, key):
    roles = []
    # {ad: x, ap: y}
    damageSplit = body['data']['champion']['damageType']
    name = body['data']['champion']['name']
    champName = champList[str(key)]
    champImgPath = '/images/champion/' + champName + '.jpg'
    champId = key
    customSkills =  body['data']['customSkills']
    # "the Mouth of the Abyss"
    title = body['data']['champion']['title']
    # {early: 3, mid: 2, late: 1} where 3 is worst, 1 is best
    powerSpike = body['data']['champion']['powerSpikes']
    for role in body['data']['roles']:
        banRate = f"{role['banRate']}%"
        lane = role['name']
        pickRate = f"{role['pickRate']}%"
        winRate = f"{role['winRate']}%"
        builds = []
        for build in role['builds']:
            # {early: ["1053"], full: ["3085", "3091", "3022"], start: ["1055", "2003", "3363"],…}
            cleanItems = {}
            items = build['items']
            cleanItems['general'] = {
                'start': getItems(items['general']['start']),
                'early': getItems(items['general']['early']),
                'core': getItems(items['general']['core']),
                'full': getItems(items['general']['full'])
            }
            cleanItems['situational'] = getItems(items['situational'][0]['build'])
            buildName = build['name']
            runes = getRunes(build['perks']['ids'], build['perks']['style'], build['perks']['subStyle'])
            spells = getSpells(build['spells'])
            skills = getSkills(build['skills']['prioritisation'], customSkills)
            build = {'items':cleanItems, 'name': buildName, 
            'runes': runes, 'spells':spells, 'skills':skills}
            builds.append(build)
        info = {'banRate': banRate, 'lane':lane, 'pickRate':pickRate, 
        'winRate':winRate, 'builds':builds}
        roles.append(info)
    champDict = {'id':key, 'name':name, 'roles': roles, 'imgPath':champImgPath}
            #https://api.mobalytics.gg/lol/champions/v1/meta?name=kogmaw
            #https://app.mobalytics.gg/lol/champions/kogmaw/build
    return champDict

def getMobalytics():
    buildList = []
    stats = []
    idx = 0
    for key, value in champList.items():
        url = f'https://api.mobalytics.gg/lol/champions/v1/meta?name={value}'
        resp = requests.get(url)
        code = resp.status_code
        if code == 200:
            body = resp.json()
            builds = cleanStats(body, key)
            buildList.append(builds)
            champName = champList[str(key)]
            champImgPath = '/images/champion/' + champName + '.jpg'
            banRate = 0.0
            pickRate = 0.0
            winRate = 0.0
            lanes = []
            for role in builds['roles']:
                banRate += float(role['banRate'][:-1])
                pickRate += float(role["pickRate"][:-1])
                winRate += float(role["winRate"][:-1])
                lanes.append(role['lane'])
            banRate = round(banRate/len(builds['roles']),1)
            pickRate = round(pickRate/len(builds['roles']),1)
            winRate = round(winRate/len(builds['roles']),1)
            stat = {'id':key, 'idx':idx, 'name':champName, 'banRate':banRate, 'lanes': lanes,
            'pickRate':pickRate, 'winRate':winRate, 'imgPath':champImgPath}
            stats.append(stat)
            idx += 1
        else:
            print(resp)
    with open('./api/dataDragon/builds.json', 'w') as json_file1:
        json.dump(buildList, json_file1, separators=(',', ':'))
    with open('./api/dataDragon/stats.json', 'w') as json_file2:
        json.dump(stats, json_file2, separators=(',', ':'))
    return buildList, stats


response_object = {'status': 'success', 'message':''}
@app.route('/api/update', methods=['GET'])
def refresh_builds():
    buildList, stats = getMobalytics()
    response_object['message'] = 'Builds refreshed!'
    response_object['builds'] = buildList
    response_object['stats'] = stats
    return jsonify(response_object)


if __name__ == '__main__':
    buildList, stats = getMobalytics()