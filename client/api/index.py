from flask import Flask, Response, jsonify, request, send_from_directory
from flask_caching import Cache
from flask_cors import CORS
import requests
import random
import json
import datetime
import operator
from math import floor

app = Flask(__name__)


response_object = {'status': 'success', 'message':''}
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (SUMMONERS), mimetype="text/html")
@app.route('/summoners', methods=['GET', 'POST'])
def all_summoners():
    if request.method == 'POST':
        post_data = request.get_json()
        accId, summId = getIds(post_data.get('name'))
        if(accId == 'Summoner not found'):
            response_object['status'] = 'failure'
            response_object['message'] = accId
        else:
            history = getHistory(accId)
            if(history == 'Match history not found'):
                response_object['status'] = 'failure'
                response_object['message'] = history
            else:
                SUMMONERS.append({
                    'id': accId,
                    'summId': summId,
                    'name': post_data.get('name'),
                    'history': history,
                    'matchInfo': getMatch(history, accId),
                    'startIndex': 0,
                    'endIndex': 10,
                    'rank': getRank(summId)
                })
                response_object['message'] = 'Summoner added!'
    else:
        #response_object['message'] = 'Summoner added!'
        response_object['summoners'] = SUMMONERS
    return jsonify(response_object)


@app.route('/summoners/<summoner_id>', methods=['PUT', 'DELETE'])
def single_summoner(summoner_id):
    response_object['status'] = 'success'
    if request.method == 'PUT':
        post_data = request.get_json()
        if(len(post_data) > 1):
            response_object['message'] = get_more_matches_summoner(summoner_id, post_data)
        else:
            response_object['message'] = replace_summoner(summoner_id, post_data)
    if request.method == 'DELETE':
        remove_summoner(summoner_id)
        response_object['message'] = 'Summoner removed!'
    return jsonify(response_object)


api_key = 'RGAPI-56ed8c86-ec30-4a32-b24b-c898c8c20267'
#fix date sort, check march dates
def getChampInfo(champId):
    champName = champList[str(champId)]
    champImgPath = '/images/champion/' + champName + '.jpg'
    return {'champName':champName, 'champImgPath':champImgPath}


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
        intScore = round((normalizedDeaths / (normalizedKills + normalizedAssists)) * 100, 2)
    else:
        intScore = random.randrange(20,400)
    return intScore


def getGameInfo(queueType, gameDuration):
    if(gameDuration > 0):
        gameLength = (int(gameDuration) / 60)
    else:
        gameLength = 0
    return {'queue':queueType, 'duration':gameLength}


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
    primaryBranch = {'keystone':keystone, 'perk1':primary1, 'perk2':primary2, 'perk3':primary3, 'name':primaryBranchName['name'], 'imgPath':primaryBranchName['imgPath']}
    secondaryBranchId = str(player['perkSubStyle'])
    secondaryBranchName = branchList[secondaryBranchId]
    secondaryBranch = {'perk0':secondary0, 'perk1':secondary1, 'name':secondaryBranchName['name'], 'imgPath':secondaryBranchName['imgPath']}
    runes['primaryBranch'] = primaryBranch
    runes['secondaryBranch'] = secondaryBranch
    return runes


def getItems(player):
    items = {}
    itemsList = []
    itemIds = [player['item0'], player['item1'], player['item2'], player['item3'], player['item4'], player['item5']]
    trinketId = player['item6']
    trinketName = itemList[str(trinketId)]
    for item in itemIds:
        if(item != 0):
            name = itemList[str(item)]
            itemsList.append(name)
    items['itemsList'] = itemsList
    items['count'] = len(itemsList) #not including trinket
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
    intScore = getIntScore(kills, deaths, assists, killsArr, deathsArr, assistsArr)
    if(deaths != 0):
        kda = round((int(kills) + int(assists)) / int(deaths), 2)
        #deathsPerMin = round(int(deaths) / gameLength,2)
    else:
        kda = 'Perfect'
        #deathsPerMin = 'N/A'
    stats = {'kills':kills, 'deaths':deaths, 'assists':assists, 'win':win, 
    'creepScore':cs, 'kda':kda, 'intScore':intScore}
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
            return  participant['participantId']


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
        summonerInfo = {'summonerName':summonerName, 'participantId':participantId,
        'champName':championInfo['champName'], 'champImgPath':championInfo['champImgPath']}
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
    redTeamTank=max(redDamageTaken.items(), key=operator.itemgetter(1))[0]
    redTeamDPS=max(redDamageDealt.items(), key=operator.itemgetter(1))[0]
    blueTeamTank=max(blueDamageTaken.items(), key=operator.itemgetter(1))[0]
    blueTeamDPS=max(blueDamageDealt.items(), key=operator.itemgetter(1))[0]
    teamInfo = {'red':redTeamInfo, 'redTeamTankIndex':redTeamTank, 'redTeamDPSIndex':redTeamDPS, 
                'blue':blueTeamInfo, 'blueTeamTankIndex':blueTeamTank, 'blueTeamDPSIndex':blueTeamDPS}
    return teamInfo


def getTeamSide(teamNumber):
    if(teamNumber == 200):
        return 'red'
    elif(teamNumber == 100):
        return 'blue'


def getMatchDate(unixTime):
    matchDate = datetime.datetime.utcfromtimestamp(unixTime/1000)
    date = str(matchDate.month) + '/' + str(matchDate.day) + '/' + str(matchDate.year)[2:]
    return date


def getMatchDuration(gameDuration):
    minutes = str(floor(gameDuration / 60))
    if(gameDuration % 60 < 10):
        seconds = '0' + str(gameDuration % 60)
    else:
        seconds = str(gameDuration % 60)
    return (minutes + ":" + seconds)


def getIds(name):
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ name +'?api_key=' + api_key
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
    url = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accId + '?endIndex='+ str(endIndex) + '&beginIndex='+ str(startIndex) + '&api_key=' + api_key
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
        url = 'https://na1.api.riotgames.com/lol/match/v4/matches/' + str(matchId) + '?api_key=' + api_key
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
        #create arrays of player stats
        killsArr, deathsArr, assistsArr = getAllStats(players)
        #iterate and find chosen player stats
        for player in players:
            if(player['participantId'] == myParticipantId):
                teamInfo = getTeamInfo(players, summonersNames)
                champInfo = getChampInfo(player['championId'])
                stats = getStats(player['stats'], killsArr, deathsArr, assistsArr)
                runes = getRunes(player['stats'])
                items = getItems(player['stats'])
                spells = getSpells(player)
                gameInfo = getGameInfo(queueType, resp['gameDuration'])
                matchInfo = {'championInfo':champInfo, 'stats':stats, 'gameInfo':gameInfo, 
                'teamInfo':teamInfo, 'runes':runes, 'items':items, 'spells':spells, 
                'matchDate':matchDate, 'matchDuration':matchDuration}
                matchArr.append(matchInfo)
                break
    return matchArr


def getRank(summId):
    url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ summId +'?api_key=' + api_key
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


#starting summoners
SUMMONERS = [
    {
        'id': '',
        'summId': '',
        'name': 'Sodhi',
        'history': [],
        'startIndex': 0,
        'endIndex': 10,
        'matchInfo': [],
        'rank': ''
    }
]

with open('api/dataDragon/champIds.json') as file1:
  champList = json.load(file1)
with open('api/dataDragon/queueIds.json') as file2:
  queueList = json.load(file2)
with open('api/dataDragon/branchIds.json') as file3:
  branchList = json.load(file3)
with open('api/dataDragon/runeIds.json') as file4:
  runeList = json.load(file4)
with open('api/dataDragon/itemIds.json') as file5:
  itemList = json.load(file5)
with open('api/dataDragon/summonerIds.json') as file6:
  spellList = json.load(file6)

def useAPI():
    for summoner in SUMMONERS:
        accountId, summonerId = getIds(summoner['name'])
        history = getHistory(accountId)
        summoner['id'] = accountId
        summoner['summId'] = summonerId
        summoner['history'] = history
        summoner['matchInfo'] = getMatch(history, accountId)
        summoner['rank'] = getRank(summonerId)

try:
    useAPI()
except Exception as ex:
    print("Exception: " + str(ex))


# configuration
DEBUG = True

# enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_summoner(summoner_id):
    for summoner in SUMMONERS:
        if summoner['id'] == summoner_id:
            SUMMONERS.remove(summoner)
            return True
    return False


def update_summoner(summoner_id, history, startIndex, endIndex, matchInfo):
    for summoner in SUMMONERS:
        if summoner['id'] == summoner_id:
            summoner['history'] += history
            summoner['startIndex'] = startIndex
            summoner['endIndex'] = endIndex
            summoner['matchInfo'] += matchInfo
            return True
    return False


def replace_summoner(summoner_id, post_data):
    remove_summoner(summoner_id)
    accId, summId = getIds(post_data.get('name'))
    history = getHistory(accId)
    SUMMONERS.append({
        'id': accId,
        'summId': summId,
        'name': post_data.get('name'),
        'history': history,
        'matchInfo': getMatch(history, accId),
        'startIndex': 0,
        'endIndex': 10,
        'rank': getRank(summId)
    })
    return 'Summoner updated!'
    

def get_more_matches_summoner(summoner_id, post_data):
    accId = post_data.get('id')
    startIndex = post_data.get('startIndex')
    endIndex = post_data.get('endIndex')
    history = getHistory(accId, startIndex, endIndex)
    matchInfo = getMatch(history, accId)
    update_summoner(summoner_id, history, startIndex, endIndex, matchInfo)
    return 'Summoner updated!'