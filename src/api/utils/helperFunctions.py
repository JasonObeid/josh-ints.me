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
from flask_cors import CORS

api_key = 'RGAPI-56ed8c86-ec30-4a32-b24b-c898c8c20267'

with open('dataDragon/champIds.json') as file1:
    champList = json.load(file1)
with open('dataDragon/queueIds.json') as file2:
    queueList = json.load(file2)
with open('dataDragon/branchIds.json') as file3:
    branchList = json.load(file3)
with open('dataDragon/runeIds.json') as file4:
    runeList = json.load(file4)
with open('dataDragon/itemIds.json') as file5:
    itemList = json.load(file5)
with open('dataDragon/summonerIds.json') as file6:
    spellList = json.load(file6)
with open('dataDragon/builds.json') as file7:
    builds = json.load(file7)
with open('dataDragon/stats.json') as file8:
    stats = json.load(file8)
with open('dataDragon/shardIds.json') as file9:
    shardList = json.load(file9)
with open('dataDragon/indexMap.json') as file10:
    indexMap = json.load(file10)
with open('dataDragon/runeMap.json') as file11:
    runeMap = json.load(file11)

#league api functions
def getChampInfo(champId):
    champName = champList[str(champId)]
    champImgPath = '/images/champion/' + champName + '.jpg'
    return {'champName': champName, 'champImgPath': champImgPath}


def getQueueName(queueId):
    queueName = queueList[str(queueId)]['description']
    return queueName


def getIntScore(kills, deaths, assists, killsArr, deathsArr, assistsArr):
    deltaKills = max(killsArr) - min(killsArr)
    deltaDeaths = max(deathsArr) - min(deathsArr)
    deltaAssists = max(assistsArr) - min(assistsArr)
    if deltaKills == 0:
        deltaKills = 1
    if deltaDeaths == 0:
        deltaDeaths = 1
    if deltaAssists == 0:
        deltaAssists = 1
    normalizedKills = (kills - min(killsArr)) / deltaKills
    normalizedDeaths = (deaths - min(deathsArr)) / deltaDeaths
    normalizedAssists = (assists - min(assistsArr)) / deltaAssists
    if(normalizedAssists != 0 or normalizedKills != 0):
        intScore = round(
            (normalizedDeaths / (normalizedKills + normalizedAssists)) * 100, 2)
    else:
        intScore = random.randrange(20, 400)
    return intScore


def getGameInfo(queueType, gameDuration):
    if(gameDuration > 0):
        gameLength = (int(gameDuration) / 60)
    else:
        gameLength = 0
    return {'queue': queueType, 'duration': gameLength}


def getRunes(player):
    runes = {}
    keystoneId = str(player['perk0'])
    keystone = runeList[keystoneId]
    primary1Id = str(player['perk1'])
    primary1 = runeList[primary1Id]
    primary2Id = str(player['perk2'])
    primary2 = runeList[primary2Id]
    primary3Id = str(player['perk3'])
    primary3 = runeList[primary3Id]
    secondary0Id = str(player['perk4'])
    secondary0 = runeList[secondary0Id]
    secondary1Id = str(player['perk5'])
    secondary1 = runeList[secondary1Id]
    primaryBranchId = str(player['perkPrimaryStyle'])
    primaryBranchName = branchList[primaryBranchId]
    primaryBranch = {'keystone': keystone, 'perk1': primary1, 'perk2': primary2, 'perk3': primary3,
                     'name': primaryBranchName['name'], 'imgPath': primaryBranchName['imgPath']}
    secondaryBranchId = str(player['perkSubStyle'])
    secondaryBranchName = branchList[secondaryBranchId]
    secondaryBranch = {'perk0': secondary0, 'perk1': secondary1,
                       'name': secondaryBranchName['name'], 'imgPath': secondaryBranchName['imgPath']}
    runes['primaryBranch'] = primaryBranch
    runes['secondaryBranch'] = secondaryBranch
    return runes


def getItems(player):
    items = {}
    itemsList = []
    itemIds = [player['item0'], player['item1'], player['item2'],
               player['item3'], player['item4'], player['item5']]
    trinketId = player['item6']
    if trinketId != 0:
        trinketName = itemList[str(trinketId)]
    else:
        trinketName = ''
    for item in itemIds:
        if item != 0 and str(item) in itemList.keys():
            name = itemList[str(item)]
            itemsList.append(name)
        else:
            name = str(item)
            itemsList.append(name)
    items['itemsList'] = itemsList
    items['count'] = len(itemsList)  # not including trinket
    items['trinket'] = trinketName
    return items


def getSpells(player):
    spells = {}
    spell1Id = str(player['spell1Id'])
    spell2Id = str(player['spell2Id'])
    spells['spell1'] = spellList[spell1Id]
    spells['spell2'] = spellList[spell2Id]
    return spells


def getStats(player, killsArr, deathsArr, assistsArr):
    kills = player['kills']
    deaths = player['deaths']
    assists = player['assists']
    win = player['win']
    cs = player['totalMinionsKilled']
    intScore = getIntScore(kills, deaths, assists,
                           killsArr, deathsArr, assistsArr)
    if(deaths != 0):
        kda = round((int(kills) + int(assists)) / int(deaths), 2)
        #deathsPerMin = round(int(deaths) / gameLength,2)
    else:
        kda = 'Perfect'
        #deathsPerMin = 'N/A'
    stats = {'kills': kills, 'deaths': deaths, 'assists': assists, 'win': win,
             'creepScore': cs, 'kda': kda, 'intScore': intScore}
    return stats


def getAllStats(players):
    killsArr = []
    deathsArr = []
    assistsArr = []
    for player in players:
        killsArr.append(int(player['stats']['kills']))
        deathsArr.append(int(player['stats']['deaths']))
        assistsArr.append(int(player['stats']['assists']))
    return [killsArr, deathsArr, assistsArr]


def getParticipantId(participantIds, accId):
    for participant in participantIds:
        accountID = participant['player']['accountId']
        if (accountID == accId):
            return participant['participantId']


def getSummonersNames(particpants):
    summonerNames = {}
    for participant in particpants:
        participantId = participant['participantId']
        summonerNames[participantId] = participant['player']['summonerName']
    return summonerNames


def getTeamInfo(players, summonerNames):
    redTeamInfo = []
    blueTeamInfo = []
    redDamageTaken = {}
    redDamageDealt = {}
    blueDamageTaken = {}
    blueDamageDealt = {}
    teamInfo = {}
    for player in players:
        participantId = player['participantId']
        summonerName = summonerNames[participantId]
        teamId = player['teamId']
        teamSide = getTeamSide(teamId)
        champId = player['championId']
        championInfo = getChampInfo(champId)
        summonerInfo = {'summonerName': summonerName, 'participantId': participantId,
                        'champName': championInfo['champName'], 'champImgPath': championInfo['champImgPath']}
        damageTaken = int(player['stats']['totalDamageTaken'])
        damageDealt = int(player['stats']['totalDamageDealtToChampions'])
        if(teamSide == 'red'):
            redTeamInfo.append(summonerInfo)
            redDamageTaken[participantId] = damageTaken
            redDamageDealt[participantId] = damageDealt
        elif(teamSide == 'blue'):
            blueTeamInfo.append(summonerInfo)
            blueDamageTaken[participantId] = damageTaken
            blueDamageDealt[participantId] = damageDealt
    redTeamTank = max(redDamageTaken.items(), key=operator.itemgetter(1))[0]
    redTeamDPS = max(redDamageDealt.items(), key=operator.itemgetter(1))[0]
    blueTeamTank = max(blueDamageTaken.items(), key=operator.itemgetter(1))[0]
    blueTeamDPS = max(blueDamageDealt.items(), key=operator.itemgetter(1))[0]
    teamInfo = {'red': redTeamInfo, 'redTeamTankIndex': redTeamTank, 'redTeamDPSIndex': redTeamDPS,
                'blue': blueTeamInfo, 'blueTeamTankIndex': blueTeamTank, 'blueTeamDPSIndex': blueTeamDPS}
    return teamInfo


def getTeamSide(teamNumber):
    if(teamNumber == 200):
        return 'red'
    elif(teamNumber == 100):
        return 'blue'


def getMatchDate(unixTime):
    matchDate = datetime.datetime.utcfromtimestamp(unixTime/1000)
    date = str(matchDate.month) + '/' + str(matchDate.day) + \
        '/' + str(matchDate.year)[2:]
    return date


def getMatchDuration(gameDuration):
    minutes = str(floor(gameDuration / 60))
    if(gameDuration % 60 < 10):
        seconds = '0' + str(gameDuration % 60)
    else:
        seconds = str(gameDuration % 60)
    return (minutes + ":" + seconds)


def getIds(name):
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + \
        name + '?api_key=' + api_key
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        accountID = body['accountId']
        summonerID = body['id']
        return accountID, summonerID
    return 'Summoner not found'


def getHistory(accId, startIndex=0, endIndex=10):
    gameArr = []
    url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accId + \
        '?endIndex=' + str(endIndex) + '&beginIndex=' + \
        str(startIndex) + '&api_key=' + api_key
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        matches = body['matches']
        for game in matches:
            gameArr.append(game['gameId'])
        return gameArr
    return 'Match history not found'


def getMatch(matchIdArr, accId):
    matchArr = []
    respArr = []
    for matchId in matchIdArr:
        url = 'https://na1.api.riotgames.com/lol/match/v4/matches/' + \
            str(matchId) + '?api_key=' + api_key
        resp = requests.get(url).json()
        respArr.append(resp)
    for resp in respArr:
        # print(resp)
        matchDate = getMatchDate(resp['gameCreation'])
        matchDuration = getMatchDuration(resp['gameDuration'])
        players = resp['participants']
        participants = resp['participantIdentities']
        myParticipantId = getParticipantId(participants, accId)
        summonersNames = getSummonersNames(participants)
        queueType = getQueueName(resp['queueId'])
        # create arrays of player stats
        killsArr, deathsArr, assistsArr = getAllStats(players)
        # iterate and find chosen player stats
        for player in players:
            if(player['participantId'] == myParticipantId):
                teamInfo = getTeamInfo(players, summonersNames)
                champInfo = getChampInfo(player['championId'])
                stats = getStats(
                    player['stats'], killsArr, deathsArr, assistsArr)
                runes = getRunes(player['stats'])
                items = getItems(player['stats'])
                spells = getSpells(player)
                gameInfo = getGameInfo(queueType, resp['gameDuration'])
                matchInfo = {'championInfo': champInfo, 'stats': stats, 'gameInfo': gameInfo,
                             'teamInfo': teamInfo, 'runes': runes, 'items': items, 'spells': spells,
                             'matchDate': matchDate, 'matchDuration': matchDuration}
                matchArr.append(matchInfo)
                break
    return matchArr


def getRank(summId):
    url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + \
        summId + '?api_key=' + api_key
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        for queueType in body:
            if queueType['queueType'] == "RANKED_SOLO_5x5":
                tier = queueType['tier']
                rank = queueType['rank']
                lp = queueType['leaguePoints']
                return f'{tier} {rank}, {lp} LP'
        return 'Unranked'
    return 'Summoner not found', 'error'


# For updating builds/stats
def getSpells2(spellIds):
    spells = []
    spell1 = spellList[str(spellIds[0])]
    spell2 = spellList[str(spellIds[1])]
    spells.append(spell1)
    spells.append(spell2)
    return spells


def getRunes2(runeIds, style, substyle):
    runes = {}
    primary = branchList[str(style)]
    secondary = branchList[str(substyle)]
    runes['primaryBranch'] = str(style)
    runes['secondaryBranch'] = str(substyle)
    runes['runes'] =  [str(runeId) for runeId in runeIds]
    return runes


def getItems2(itemIds):
    itemsList = []
    for item in itemIds:
        if(item != 0 and str(item) in itemList.keys()):
            name = itemList[str(item)]
            itemsList.append(name)
        else:
            name = str(item)
            itemsList.append(name)
    return itemsList


def getSkills2(order, customSkills):
    skills = []
    skillMap = {'Q': 1, 'W': 2, 'E': 3, 'R': 4}
    for skill in order:
        skillIndex = skillMap[skill]
        name = customSkills[skillIndex]['name']
        imgPath = 'images/spell/' + customSkills[skillIndex]['image'] + '.jpg'
        skills.append({'name': name, 'imgPath': imgPath, 'button': skill})
    return skills


def cleanStats(body, key):
    roles = []
    # {ad: x, ap: y}
    #damageSplit = body['data']['champion']['damageType']
    name = body['data']['champion']['name']
    champName = champList[str(key)]
    champImgPath = '/images/champion/' + champName + '.jpg'
    #champId = key
    customSkills = body['data']['customSkills']
    # "the Mouth of the Abyss"
    # title = body['data']['champion']['title']
    # {early: 3, mid: 2, late: 1} where 3 is worst, 1 is best
    #powerSpike = body['data']['champion']['powerSpikes']
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
                'start': getItems2(items['general']['start']),
                'early': getItems2(items['general']['early']),
                'core': getItems2(items['general']['core']),
                'full': getItems2(items['general']['full'])
            }
            cleanItems['situational'] = getItems2(
                items['situational'][0]['build'])
            buildName = build['name']
            runes = getRunes2(
                build['perks']['ids'], build['perks']['style'], build['perks']['subStyle'])
            spells = getSpells2(build['spells'])
            skills = getSkills2(
                build['skills']['prioritisation'], customSkills)
            build = {'items': cleanItems, 'name': buildName,
                     'runes': runes, 'spells': spells, 'skills': skills}
            builds.append(build)
        info = {'banRate': banRate, 'lane': lane, 'pickRate': pickRate,
                'winRate': winRate, 'builds': builds}
        roles.append(info)
    champDict = {'id': key, 'name': name,
                 'roles': roles, 'imgPath': champImgPath}
    # https://api.mobalytics.gg/lol/champions/v1/meta?name=kogmaw
    # https://app.mobalytics.gg/lol/champions/kogmaw/build
    return champDict


def getMobalytics():
    buildList = []
    stats = []
    indexMap = {}
    idx = 0
    for key, value in champList.items():
        url = f'https://api.mobalytics.gg/lol/champions/v1/meta?name={value}'
        resp = requests.get(url)
        code = resp.status_code
        if code == 200:
            try:
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
                indexMap[champName.lower()] = idx
                print(f'{champName} okay')
                idx += 1
            except Exception as err:
                print("err", champList[str(key)])
        else:
            print(resp)
    with open('dataDragon/builds.json', 'w') as json_file1:
        json.dump(buildList, json_file1, separators=(',', ':'))
    with open('dataDragon/stats.json', 'w') as json_file2:
        json.dump(stats, json_file2, separators=(',', ':'))
    with open('dataDragon/indexMap.json', 'w') as json_file3:
        json.dump(indexMap, json_file3, separators=(',', ':'))
    return buildList, stats

"""def getItemsTrinket(itemIds, trinketId):
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
    return items"""

