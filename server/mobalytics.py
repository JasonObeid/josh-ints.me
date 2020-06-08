
import requests
from collections import Counter
import csv
import json
from statistics import mean, mode

with open('../dataDragon/champIds.json') as file1:
    champList = json.load(file1)
with open('../dataDragon/branchIds.json') as file3:
    branchList = json.load(file3)
with open('../dataDragon/runeIds.json') as file4:
    runeList = json.load(file4)
with open('../dataDragon/itemIds.json') as file5:
    itemList = json.load(file5)
with open('../dataDragon/shardIds.json') as file6:
    shardList = json.load(file6)

def getSpells(spellIds):
    return [spellIds[0][0], spellIds[1][0]]

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
    print(itemIds)
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

def cleanStats(body, key):
    roles = []
    # {ad: x, ap: y}
    damageSplit = body['data']['champion']['damageType']
    name = body['data']['champion']['name']
    champId = key
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
            build = {'items':cleanItems, 'name': buildName, 'runes': runes, 'spells':spells}
            builds.append(build)
        info = {'banRate': banRate, 'lane':lane, 'pickRate':pickRate, 
        'winRate':winRate, 'builds':builds}
        roles.append(info)
    champDict = {'id':key, 'name':name, 'roles': roles}
            #https://api.mobalytics.gg/lol/champions/v1/meta?name=kogmaw
            #https://app.mobalytics.gg/lol/champions/kogmaw/build
    return champDict

def getMobalytics():
    buildList = []
    stats = []
    for key, value in champList.items():
        url = f'https://api.mobalytics.gg/lol/champions/v1/meta?name={value}'
        resp = requests.get(url)
        code = resp.status_code
        if code == 200:
            body = resp.json()
            builds = cleanStats(body, key)
            buildList.append(builds)
            stats.append(champList[key])
            #print(body)
        else:
            print(resp)
    with open('./builds.json', 'w') as json_file1:
        json.dump(buildList, json_file1, indent=3)
    with open('./stats.json', 'w') as json_file2:
        json.dump(stats, json_file2, indent=3)

getMobalytics()