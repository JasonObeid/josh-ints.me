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

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

api_key = 'RGAPI-56ed8c86-ec30-4a32-b24b-c898c8c20267'
# fix date sort, check march dates


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
        if(item != 0):
            name = itemList[str(item)]
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
        resp = requests.get(url)
        code = resp.status_code
        if code == 200:
            body = resp.json()
            respArr.append(body)
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


def getRuneIds(player):
    keystone = str(player['perk0'])
    primary1 = str(player['perk1'])
    primary2 = str(player['perk2'])
    primary3 = str(player['perk3'])
    secondary0 = str(player['perk4'])
    secondary1 = str(player['perk5'])
    primaryBranchId = str(player['perkPrimaryStyle'])
    primaryBranch = (primaryBranchId, keystone, primary1, primary2, primary3)
    secondaryBranchId = str(player['perkSubStyle'])
    secondaryBranch = (secondaryBranchId, secondary0, secondary1)
    runes = (primaryBranch, secondaryBranch)
    return runes


def getItemIds(player):
    itemIds = (player['item0'], player['item1'], player['item2'],
               player['item3'], player['item4'], player['item5'])
    trinketId = player['item6']
    items = (itemIds, trinketId)
    return items


def getSpellIds(player):
    spell1Id = str(player['spell1Id'])
    spell2Id = str(player['spell2Id'])
    spells = (spell1Id, spell2Id)
    return spells


def getChallengerHistory(accId, startIndex=0, endIndex=10):
    gameArr = []
    queueId = '420'
    seasonId = '13'
    url = f'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{accId}?queue={queueId}&season={seasonId}&endIndex={endIndex}&api_key={api_key}'
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        matches = body['matches']
        print(code)
        for game in matches:
            gameArr.append(game['gameId'])
        return gameArr
    return 'Match history not found'


def getMasterPlayers():
    playerList = []
    requestCount = 0
    mastersUrl = 'https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5' + \
        '?api_key=' + api_key
    gmastersUrl = 'https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5' + '?api_key=' + api_key
    challengersUrl = 'https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5' + '?api_key=' + api_key
    with open('accounts.txt', mode='w') as accountsFile:
        for league in [challengersUrl, mastersUrl, gmastersUrl]:
            try:
                resp = requests.get(league)
                requestCount += 1
                if requestCount + 1 > 100:
                    requestCount = 0
                    print('waiting')
                    time.sleep(130)
                code = resp.status_code
                if code == 200:
                    body = resp.json()
                    # get summoner ids
                    for player in body['entries']:
                        accountId = getIds(player['summonerName'])[0]
                        requestCount += 1
                        if requestCount + 1 > 100:
                            requestCount = 0
                            print('waiting')
                            time.sleep(130)
                        if accountId != 'Summoner not found':
                            playerList.append(accountId)
                            accountsFile.write(f"{accountId}\n")
            except Exception as e:
                print(f'exception {e} at line {sys.exc_info()[-1].tb_lineno}')
                continue
    print(len(playerList))
    return playerList


def getMasterHistory(playerList):
    requestCount = 0
    historyList = []
    with open('matches.txt', mode='a') as matchesFile:
        for accountId in playerList:
            try:
                matchIds = getChallengerHistory(accountId)
                requestCount += 1
                if requestCount + 1 > 100:
                    requestCount = 0
                    print('waiting')
                    time.sleep(130)
                print(matchIds)
                if matchIds != 'Match history not found':
                    for match in matchIds:
                        if match not in historyList:
                            historyList.append(str(match))
                            matchesFile.write(f"{match}\n")
            except Exception as e:
                print(f'exception {e} at line {sys.exc_info()[-1].tb_lineno}')
                continue
    time.sleep(130)
    return historyList


def getChampions(historyList):
    requestCount = 0
    with open('entries.csv', mode='a+', newline='') as statsFile:
        writer = csv.writer(statsFile, delimiter=',')
        for matchId in historyList:
            try:
                matchInfo = getMatchInfo(matchId)
                requestCount += 1
                if requestCount + 1 > 100:
                    requestCount = 0
                    print('waiting')
                    time.sleep(130)
                for champ in matchInfo:
                    champStats = []
                    stats = champ[1]
                    # id
                    champStats.append(champ[0])
                    # stats
                    champStats.append(int(stats['kills']))
                    champStats.append(int(stats['assists']))
                    champStats.append(int(stats['deaths']))
                    champStats.append(int(stats['creepScore']))
                    champStats.append(bool(stats['win']))
                    # primary
                    champStats.append(int(champ[2][0][0]))
                    champStats.append(int(champ[2][0][1]))
                    champStats.append(int(champ[2][0][2]))
                    champStats.append(int(champ[2][0][3]))
                    champStats.append(int(champ[2][0][4]))
                    # secondary
                    champStats.append(int(champ[2][1][0]))
                    champStats.append(int(champ[2][1][1]))
                    champStats.append(int(champ[2][1][2]))
                    # items
                    champStats.append(int(champ[3][0][0]))
                    champStats.append(int(champ[3][0][1]))
                    champStats.append(int(champ[3][0][2]))
                    champStats.append(int(champ[3][0][3]))
                    champStats.append(int(champ[3][0][4]))
                    champStats.append(int(champ[3][0][5]))
                    # trinket
                    champStats.append(int(champ[3][1]))
                    # summoner spells
                    champStats.append(int(champ[4][0]))
                    champStats.append(int(champ[4][1]))
                    writer.writerow(champStats)
            except KeyError as e:
                print(f'KeyError {e} at line {sys.exc_info()[-1].tb_lineno}')
                continue


# todo, write to file on each loop to reduce memory
def getMasterMatches():
    try:
        # get top players
        playerList = getMasterPlayers()
        # get matches for each summoner
        historyList = getMasterHistory(playerList)
        print(len(historyList))
        # with open('matches.txt', mode='r') as matchesFile:
        #     historyList = [line.strip() for line in matchesFile.readlines()]
        # remove duplicates
        historyList = list(dict.fromkeys(historyList))
        # get match details for each match in history
        getChampions(historyList)
        writeTopItems()
    except Exception as e:
        print('Error on line {}'.format(
            sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

# todo look into KeyError 'perkSubStyle' in roughly every 250 matches

def getMatchInfo(matchId):
    playerStats = []
    url = 'https://na1.api.riotgames.com/lol/match/v4/matches/' + \
        str(matchId) + '?api_key=' + api_key
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        #matchDuration = getMatchDuration(resp['gameDuration'])
        players = body['participants']
        # create arrays of player stats
        killsArr, deathsArr, assistsArr = getAllStats(players)
        # iterate and find chosen player stats
        for player in players:
            champId = player['championId']
            stats = getStats(player['stats'], killsArr, deathsArr, assistsArr)
            runes = getRuneIds(player['stats'])
            items = getItemIds(player['stats'])
            spells = getSpellIds(player)
            matchDict = (champId, stats, runes, items, spells)
            playerStats.append(matchDict)
    return playerStats


def writeTopItems():
    with open('./entries_2.csv', mode='r', newline='') as statsFile:
        reader = csv.reader(statsFile, delimiter=',')
        rows = [line for line in reader]

    with open('./stats.json', 'w') as json_file:
        champDict = {}
        for champId in champList.keys():
            kills = []
            assists = []
            deaths = []
            wins = 0
            cs = []
            primary = []
            secondary = []
            items = []
            trinket = []
            spells = []
            for row in rows:
                if row[0] == champId:
                    if row[5] == 'True':
                        wins += 1
                    kills.append(int(row[1]))
                    assists.append(int(row[2]))
                    deaths.append(int(row[3]))
                    cs.append(int(row[4]))
                    primaries = tuple(int(x) for x in row[6:10])
                    primary.append(primaries)
                    secondaries = tuple(int(x) for x in row[11:13])
                    secondary.append(secondaries)
                    item = tuple(int(x) for x in row[14:19])
                    items.append(item)
                    trinket.append(int(row[20]))
                    summSpells = tuple(int(x) for x in row[21:])
                    spells.append(summSpells[0])
                    spells.append(summSpells[1])
            if len(kills) > 0:
                topPrimary = Counter(primary).most_common(2)
                topSecondary = Counter(secondary).most_common(2)
                topSpells = Counter(spells).most_common(2)
                stats = {'kills': mean(kills), 'deaths': mean(deaths), 'cs': mean(cs), 'wins':f'{round((wins/len(kills)*100),1)}%'}
                runes = getRunes2(topPrimary, topSecondary)
                items = getItems2(mode(items),  mode(trinket))
                spells = getSpells2(topSpells)
                championInfo = getChampInfo(champId)
                champDict[champId] = {'championInfo':championInfo, 'samples': len(kills), 'stats':stats,
                        'items': items, 'runes': runes, 'spells': spells}
        json.dump(champDict, json_file, indent=3)


def getSpells2(spellIds):
    spells = {}
    spells['spell1'] = spellIds[0][0]
    spells['spell2'] = spellIds[1][0]
    return spells


def getItems2(itemIds, trinketId):
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


def getRunes2(topPrimary, topSecondary):
    runes = {}
    print(topPrimary, topSecondary)
    for optionPrimary, optionSecondary, i in zip(topPrimary, topSecondary, range(len(topPrimary))):
        optionPrimary = optionPrimary[0]
        optionSecondary = optionSecondary[0]
        option = {}
        keystoneId = '8112'#str(optionPrimary[0])
        keystone = runeList[keystoneId]
        primary1Id = str(optionPrimary[1])
        primary1 = runeList[primary1Id]
        primary2Id = str(optionPrimary[2])
        primary2 = runeList[primary2Id]
        primary3Id = str(optionPrimary[3])
        primary3 = runeList[primary3Id]
        secondary0Id = '8345' # str(optionSecondary[0])
        secondary0 = runeList[secondary0Id]
        secondary1Id = str(optionSecondary[1])
        secondary1 = runeList[secondary1Id]
        for key, value in branchList.items():
            if keystoneId[:2] in key:
                primaryBranchName = value
            if secondary0Id[:2] in key:
                secondaryBranchName = value
        primaryBranch = {'keystone': keystone, 'perk1': primary1, 'perk2': primary2, 'perk3': primary3,
                        'name': primaryBranchName['name'], 'imgPath': primaryBranchName['imgPath']}
        secondaryBranch = {'perk0': secondary0, 'perk1': secondary1,
                        'name': secondaryBranchName['name'], 'imgPath': secondaryBranchName['imgPath']}
        option['primaryBranch'] = primaryBranch
        option['secondaryBranch'] = secondaryBranch
        runes[i] = option
    return runes

# starting summoners
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

with open('../dataDragon/champIds.json') as file1:
    champList = json.load(file1)
with open('../dataDragon/queueIds.json') as file2:
    queueList = json.load(file2)
with open('../dataDragon/branchIds.json') as file3:
    branchList = json.load(file3)
with open('../dataDragon/runeIds.json') as file4:
    runeList = json.load(file4)
with open('../dataDragon/itemIds.json') as file5:
    itemList = json.load(file5)
with open('../dataDragon/summonerIds.json') as file6:
    spellList = json.load(file6)
with open('../dataDragon/stats.json') as file7:
    builds = json.load(file7)

def useAPI():
    for summoner in SUMMONERS:
        accountId, summonerId = getIds(summoner['name'])
        history = getHistory(accountId)
        summoner['id'] = accountId
        summoner['summId'] = summonerId
        summoner['history'] = history
        summoner['matchInfo'] = getMatch(history, accountId)
        summoner['rank'] = getRank(summonerId)


#getMasterMatches()

try:
    useAPI()
except Exception as e:
    print('Error on line {}'.format(
        sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


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


response_object = {'status': 'success', 'message': ''}
    
@app.route('/builds', methods=['GET'])
def get_builds():
    print('HERE ')
    response_object['message'] = 'Summoner added!'
    response_object['builds'] = builds
    # response_object['champs'] = champList
    return jsonify(response_object)


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
            response_object['message'] = get_more_matches_summoner(
                summoner_id, post_data)
        else:
            response_object['message'] = replace_summoner(
                summoner_id, post_data)
    if request.method == 'DELETE':
        remove_summoner(summoner_id)
        response_object['message'] = 'Summoner removed!'
    return jsonify(response_object)


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


""" @app.route('/summoners', methods=['GET'])
def refreshAll():
    response_object = {'status': 'success'}
    matchArray = []
    if request.method == 'GET':
        for summoner in SUMMONERS:
            summoner['history'] = getHistory(summoner['id'])
            for match in summoner['history']:
                matchArray.append(getMatch(match, summoner['id']))
            summoner['matchInfo'] = matchArray
        response_object['summoners'] = SUMMONERS """


if __name__ == '__main__':
    app.run()
