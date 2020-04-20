from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
import random
import json
import datetime
from math import floor

api_key = 'RGAPI-56ed8c86-ec30-4a32-b24b-c898c8c20267'

def getChampInfo(champId):
    champName = champList[str(champId)]
    champImgPath = '/images/champion/' + champName + '.png'
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


def getParticipantId(particpantIds, accId):
    for participant in particpantIds:
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
    teamInfo = {}
    for player in players:
        participantId = player['participantId']
        summonerName = summonerNames[participantId]
        teamId = player['teamId']
        teamSide = getTeamSide(teamId)
        champId = player['championId']
        championInfo = getChampInfo(champId)
        summonerInfo = {'summonerName':summonerName, 'particpantId':participantId,
        'champName':championInfo['champName'], 'champImgPath':championInfo['champImgPath']}
        if(teamSide == 'red'):
            redTeamInfo.append(summonerInfo)
        elif(teamSide == 'blue'):
            blueTeamInfo.append(summonerInfo)
    teamInfo = {'red':redTeamInfo, 'blue':blueTeamInfo}
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


def getId(name):
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ name +'?api_key=' + api_key
    resp = requests.get(url)
    code = resp.status_code
    if code == 200:
        body = resp.json()
        accountID = body['accountId']
        return accountID
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


SUMMONERS = [
    {
        'id': '',
        'name': 'Sodhi',
        'history': [],
        'startIndex': 0,
        'endIndex': 10,
        'matchInfo': []
    }
]

champList = {"266": "Aatrox", "103": "Ahri", "84": "Akali", "12": "Alistar", "32": "Amumu", "34": "Anivia", "1": "Annie", "523": "Aphelios", "22": "Ashe", "136": "AurelionSol", "268": "Azir", "432": "Bard", "53": "Blitzcrank", "63": "Brand", "201": "Braum", "51": "Caitlyn", "164": "Camille", "69": "Cassiopeia", "31": "Chogath", "42": "Corki", "122": "Darius", "131": "Diana", "119": "Draven", "36": "DrMundo", "245": "Ekko", "60": "Elise", "28": "Evelynn", "81": "Ezreal", "9": "Fiddlesticks", "114": "Fiora", "105": "Fizz", "3": "Galio", "41": "Gangplank", "86": "Garen", "150": "Gnar", "79": "Gragas", "104": "Graves", "120": "Hecarim", "74": "Heimerdinger", "420": "Illaoi", "39": "Irelia", "427": "Ivern", "40": "Janna", "59": "JarvanIV", "24": "Jax", "126": "Jayce", "202": "Jhin", "222": "Jinx", "145": "Kaisa", "429": "Kalista", "43": "Karma", "30": "Karthus", "38": "Kassadin", "55": "Katarina", "10": "Kayle", "141": "Kayn", "85": "Kennen", "121": "Khazix", "203": "Kindred", "240": "Kled", "96": "KogMaw", "7": "Leblanc", "64": "LeeSin", "89": "Leona", "127": "Lissandra", "236": "Lucian", "117": "Lulu", "99": "Lux", "54": "Malphite", "90": "Malzahar", "57": "Maokai", "11": "MasterYi", "21": "MissFortune", "62": "MonkeyKing", "82": "Mordekaiser", "25": "Morgana", "267": "Nami", "75": "Nasus", "111": "Nautilus", "518": "Neeko", "76": "Nidalee", "56": "Nocturne", "20": "Nunu", "2": "Olaf", "61": "Orianna", "516": "Ornn", "80": "Pantheon", "78": "Poppy", "555": "Pyke", "246": "Qiyana", "133": "Quinn", "497": "Rakan", "33": "Rammus", "421": "RekSai", "58": "Renekton", "107": "Rengar", "92": "Riven", "68": "Rumble", "13": "Ryze", "113": "Sejuani", "235": "Senna", "875": "Sett", "35": "Shaco", "98": "Shen", "102": "Shyvana", "27": "Singed", "14": "Sion", "15": "Sivir", "72": "Skarner", "37": "Sona", "16": "Soraka", "50": "Swain", "517": "Sylas", "134": "Syndra", "223": "TahmKench", "163": "Taliyah", "91": "Talon", "44": "Taric", "17": "Teemo", "412": "Thresh", "18": "Tristana", "48": "Trundle", "23": "Tryndamere", "4": "TwistedFate", "29": "Twitch", "77": "Udyr", "6": "Urgot", "110": "Varus", "67": "Vayne", "45": "Veigar", "161": "Velkoz", "254": "Vi", "112": "Viktor", "8": "Vladimir", "106": "Volibear", "19": "Warwick", "498": "Xayah", "101": "Xerath", "5": "XinZhao", "157": "Yasuo", "83": "Yorick", "350": "Yuumi", "154": "Zac", "238": "Zed", "115": "Ziggs", "26": "Zilean", "142": "Zoe", "143": "Zyra"}
queueList = {"0": {"map": "Custom games", "description": "Custom"}, "2": {"map": "Summoner's Rift", "description": "5v5 Blind Pick"}, "4": {"map": "Summoner's Rift", "description": "5v5 Ranked Solo"}, "6": {"map": "Summoner's Rift", "description": "5v5 Ranked Premade"}, "7": {"map": "Summoner's Rift", "description": "Co-op vs AI"}, "8": {"map": "Twisted Treeline", "description": "3v3 Normal"}, "9": {"map": "Twisted Treeline", "description": "3v3 Ranked Flex"}, "14": {"map": "Summoner's Rift", "description": "5v5 Draft Pick"}, "16": {"map": "Crystal Scar", "description": "5v5 Dominion Blind Pick"}, "17": {"map": "Crystal Scar", "description": "5v5 Dominion Draft Pick"}, "25": {"map": "Crystal Scar", "description": "Dominion Co-op vs AI"}, "31": {"map": "Summoner's Rift", "description": "Co-op vs AI Intro Bot"}, "32": {"map": "Summoner's Rift", "description": "Co-op vs AI Beginner Bot"}, "33": {"map": "Summoner's Rift", "description": "Co-op vs AI Intermediate Bot"}, "41": {"map": "Twisted Treeline", "description": "3v3 Ranked Team"}, "42": {"map": "Summoner's Rift", "description": "5v5 Ranked Team"}, "52": {"map": "Twisted Treeline", "description": "Co-op vs AI"}, "61": {"map": "Summoner's Rift", "description": "5v5 Team Builder"}, "65": {"map": "Howling Abyss", "description": "5v5 ARAM"}, "67": {"map": "Howling Abyss", "description": "ARAM Co-op vs AI"}, "70": {"map": "Summoner's Rift", "description": "One for All"}, "72": {"map": "Howling Abyss", "description": "1v1 Snowdown Showdown"}, "73": {"map": "Howling Abyss", "description": "2v2 Snowdown Showdown"}, "75": {"map": "Summoner's Rift", "description": "6v6 Hexakill"}, "76": {"map": "Summoner's Rift", "description": "Ultra Rapid Fire"}, "78": {"map": "Howling Abyss", "description": "One For All: Mirror Mode"}, "83": {"map": "Summoner's Rift", "description": "Co-op vs AI Ultra Rapid Fire"}, "91": {"map": "Summoner's Rift", "description": "Doom Bots Rank 1"}, "92": {"map": "Summoner's Rift", "description": "Doom Bots Rank 2"}, "93": {"map": "Summoner's Rift", "description": "Doom Bots Rank 5"}, "96": {"map": "Crystal Scar", "description": "Ascension"}, "98": {"map": "Twisted Treeline", "description": "6v6 Hexakill"}, "100": {"map": "Butcher's Bridge", "description": "5v5 ARAM"}, "300": {"map": "Howling Abyss", "description": "Legend of the Poro King"}, "310": {"map": "Summoner's Rift", "description": "Nemesis"}, "313": {"map": "Summoner's Rift", "description": "Black Market Brawlers"}, "315": {"map": "Summoner's Rift", "description": "Nexus Siege"}, "317": {"map": "Crystal Scar", "description": "Definitely Not Dominion"}, "318": {"map": "Summoner's Rift", "description": "ARURF"}, "325": {"map": "Summoner's Rift", "description": "All Random"}, "400": {"map": "Summoner's Rift", "description": "5v5 Draft Pick"}, "410": {"map": "Summoner's Rift", "description": "5v5 Ranked Dynamic"}, "420": {"map": "Summoner's Rift", "description": "5v5 Ranked Solo"}, "430": {"map": "Summoner's Rift", "description": "5v5 Blind Pick"}, "440": {"map": "Summoner's Rift", "description": "5v5 Ranked Flex"}, "450": {"map": "Howling Abyss", "description": "5v5 ARAM"}, "460": {"map": "Twisted Treeline", "description": "3v3 Blind Pick"}, "470": {"map": "Twisted Treeline", "description": "3v3 Ranked Flex"}, "600": {"map": "Summoner's Rift", "description": "Blood Hunt Assassin"}, "610": {"map": "Cosmic Ruins", "description": "Dark Star: Singularity"}, "700": {"map": "Summoner's Rift", "description": "Clash"}, "800": {"map": "Twisted Treeline", "description": "Co-op vs. AI Intermediate Bot"}, "810": {"map": "Twisted Treeline", "description": "Co-op vs. AI Intro Bot"}, "820": {"map": "Twisted Treeline", "description": "Co-op vs. AI Beginner Bot"}, "830": {"map": "Summoner's Rift", "description": "Co-op vs. AI Intro Bot"}, "840": {"map": "Summoner's Rift", "description": "Co-op vs. AI Beginner Bot"}, "850": {"map": "Summoner's Rift", "description": "Co-op vs. AI Intermediate Bot"}, "900": {"map": "Summoner's Rift", "description": "URF"}, "910": {"map": "Crystal Scar", "description": "Ascension"}, "920": {"map": "Howling Abyss", "description": "Legend of the Poro King"}, "940": {"map": "Summoner's Rift", "description": "Nexus Siege"}, "950": {"map": "Summoner's Rift", "description": "Doom Bots Voting"}, "960": {"map": "Summoner's Rift", "description": "Doom Bots Standard"}, "980": {"map": "Valoran City Park", "description": "Star Guardian Invasion: Normal"}, "990": {"map": "Valoran City Park", "description": "Star Guardian Invasion: Onslaught"}, "1000": {"map": "Overcharge", "description": "PROJECT: Hunters"}, "1010": {"map": "Summoner's Rift", "description": "Snow ARURF"}, "1020": {"map": "Summoner's Rift", "description": "One for All"}, "1030": {"map": "Crash Site", "description": "Odyssey Extraction: Intro"}, "1040": {"map": "Crash Site", "description": "Odyssey Extraction: Cadet"}, "1050": {"map": "Crash Site", "description": "Odyssey Extraction: Crewmember"}, "1060": {"map": "Crash Site", "description": "Odyssey Extraction: Captain"}, "1070": {"map": "Crash Site", "description": "Odyssey Extraction: Onslaught"}, "1090": {"map": "Convergence", "description": "Teamfight Tactics"}, "1100": {"map": "Convergence", "description": "Ranked Teamfight Tactics"}, "1110": {"map": "Convergence", "description": "Teamfight Tactics Tutorial"}, "1200": {"map": "Nexus Blitz", "description": "Nexus Blitz"}, "2000": {"map": "Summoner's Rift", "description": "Tutorial 1"}, "2010": {"map": "Summoner's Rift", "description": "Tutorial 2"}, "2020": {"map": "Summoner's Rift", "description": "Tutorial 3"}}
branchList = {"8100": {"name": "Domination", "imgPath": "images/runes/Domination.png"}, "8300": {"name": "Inspiration", "imgPath": "images/runes/Inspiration.png"}, "8000": {"name": "Precision", "imgPath": "images/runes/Precision.png"}, "8400": {"name": "Resolve", "imgPath": "images/runes/Resolve.png"}, "8200": {"name": "Sorcery", "imgPath": "images/runes/Sorcery.png"}}
runeList = {"8112": {"name": "Electrocute", "imgPath": "images/runes/Domination/Electrocute/Electrocute.png"}, "8124": {"name": "Predator", "imgPath": "images/runes/Domination/Predator/Predator.png"}, "8128": {"name": "DarkHarvest", "imgPath": "images/runes/Domination/DarkHarvest/DarkHarvest.png"}, "9923": {"name": "HailOfBlades", "imgPath": "images/runes/Domination/HailOfBlades/HailOfBlades.png"}, "8126": {"name": "CheapShot", "imgPath": "images/runes/Domination/CheapShot/CheapShot.png"}, "8139": {"name": "TasteOfBlood", "imgPath": "images/runes/Domination/TasteOfBlood/TasteOfBlood.png"}, "8143": {"name": "SuddenImpact", "imgPath": "images/runes/Domination/SuddenImpact/SuddenImpact.png"}, "8136": {"name": "ZombieWard", "imgPath": "images/runes/Domination/ZombieWard/ZombieWard.png"}, "8120": {"name": "GhostPoro", "imgPath": "images/runes/Domination/GhostPoro/GhostPoro.png"}, "8138": {"name": "EyeballCollection", "imgPath": "images/runes/Domination/EyeballCollection/EyeballCollection.png"}, "8135": {"name": "RavenousHunter", "imgPath": "images/runes/Domination/RavenousHunter/RavenousHunter.png"}, "8134": {"name": "IngeniousHunter", "imgPath": "images/runes/Domination/IngeniousHunter/IngeniousHunter.png"}, "8105": {"name": "RelentlessHunter", "imgPath": "images/runes/Domination/RelentlessHunter/RelentlessHunter.png"}, "8106": {"name": "UltimateHunter", "imgPath": "images/runes/Domination/UltimateHunter/UltimateHunter.png"}, "8351": {"name": "GlacialAugment", "imgPath": "images/runes/Inspiration/GlacialAugment/GlacialAugment.png"}, "8360": {"name": "UnsealedSpellbook", "imgPath": "images/runes/Inspiration/UnsealedSpellbook/UnsealedSpellbook.png"}, "8358": {"name": "MasterKey", "imgPath": "images/runes/Inspiration/MasterKey/MasterKey.png"}, "8306": {"name": "HextechFlashtraption", "imgPath": "images/runes/Inspiration/HextechFlashtraption/HextechFlashtraption.png"}, "8304": {"name": "MagicalFootwear", "imgPath": "images/runes/Inspiration/MagicalFootwear/MagicalFootwear.png"}, "8313": {"name": "PerfectTiming", "imgPath": "images/runes/Inspiration/PerfectTiming/PerfectTiming.png"}, "8321": {"name": "FuturesMarket", "imgPath": "images/runes/Inspiration/FuturesMarket/FuturesMarket.png"}, "8316": {"name": "MinionDematerializer", "imgPath": "images/runes/Inspiration/MinionDematerializer/MinionDematerializer.png"}, "8345": {"name": "BiscuitDelivery", "imgPath": "images/runes/Inspiration/BiscuitDelivery/BiscuitDelivery.png"}, "8347": {"name": "CosmicInsight", "imgPath": "images/runes/Inspiration/CosmicInsight/CosmicInsight.png"}, "8410": {"name": "ApproachVelocity", "imgPath": "images/runes/Inspiration/ApproachVelocity/ApproachVelocity.png"}, "8352": {"name": "TimeWarpTonic", "imgPath": "images/runes/Inspiration/TimeWarpTonic/TimeWarpTonic.png"}, "8005": {"name": "PressTheAttack", "imgPath": "images/runes/Precision/PressTheAttack/PressTheAttack.png"}, "8008": {"name": "LethalTempo", "imgPath": "images/runes/Precision/LethalTempo/LethalTempo.png"}, "8021": {"name": "FleetFootwork", "imgPath": "images/runes/Precision/FleetFootwork/FleetFootwork.png"}, "8010": {"name": "Conqueror", "imgPath": "images/runes/Precision/Conqueror/Conqueror.png"}, "9101": {"name": "Overheal", "imgPath": "images/runes/Precision/Overheal/Overheal.png"}, "9111": {"name": "Triumph", "imgPath": "images/runes/Precision/Triumph/Triumph.png"}, "8009": {"name": "PresenceOfMind", "imgPath": "images/runes/Precision/PresenceOfMind/PresenceOfMind.png"}, "9104": {"name": "LegendAlacrity", "imgPath": "images/runes/Precision/LegendAlacrity/LegendAlacrity.png"}, "9105": {"name": "LegendTenacity", "imgPath": "images/runes/Precision/LegendTenacity/LegendTenacity.png"}, "9103": {"name": "LegendBloodline", "imgPath": "images/runes/Precision/LegendBloodline/LegendBloodline.png"}, "8014": {"name": "CoupDeGrace", "imgPath": "images/runes/Precision/CoupDeGrace/CoupDeGrace.png"}, "8017": {"name": "CutDown", "imgPath": "images/runes/Precision/CutDown/CutDown.png"}, "8299": {"name": "LastStand", "imgPath": "images/runes/Precision/LastStand/LastStand.png"}, "8437": {"name": "GraspOfTheUndying", "imgPath": "images/runes/Resolve/GraspOfTheUndying/GraspOfTheUndying.png"}, "8439": {"name": "Aftershock", "imgPath": "images/runes/Resolve/Aftershock/Aftershock.png"}, "8465": {"name": "Guardian", "imgPath": "images/runes/Resolve/Guardian/Guardian.png"}, "8446": {"name": "Demolish", "imgPath": "images/runes/Resolve/Demolish/Demolish.png"}, "8463": {"name": "FontOfLife", "imgPath": "images/runes/Resolve/FontOfLife/FontOfLife.png"}, "8401": {"name": "ShieldBash", "imgPath": "images/runes/Resolve/ShieldBash/ShieldBash.png"}, "8429": {"name": "Conditioning", "imgPath": "images/runes/Resolve/Conditioning/Conditioning.png"}, "8444": {"name": "SecondWind", "imgPath": "images/runes/Resolve/SecondWind/SecondWind.png"}, "8473": {"name": "BonePlating", "imgPath": "images/runes/Resolve/BonePlating/BonePlating.png"}, "8451": {"name": "Overgrowth", "imgPath": "images/runes/Resolve/Overgrowth/Overgrowth.png"}, "8453": {"name": "Revitalize", "imgPath": "images/runes/Resolve/Revitalize/Revitalize.png"}, "8242": {"name": "Unflinching", "imgPath": "images/runes/Resolve/Unflinching/Unflinching.png"}, "8214": {"name": "SummonAery", "imgPath": "images/runes/Sorcery/SummonAery/SummonAery.png"}, "8229": {"name": "ArcaneComet", "imgPath": "images/runes/Sorcery/ArcaneComet/ArcaneComet.png"}, "8230": {"name": "PhaseRush", "imgPath": "images/runes/Sorcery/PhaseRush/PhaseRush.png"}, "8224": {"name": "NullifyingOrb", "imgPath": "images/runes/Sorcery/NullifyingOrb/NullifyingOrb.png"}, "8226": {"name": "ManaflowBand", "imgPath": "images/runes/Sorcery/ManaflowBand/ManaflowBand.png"}, "8275": {"name": "NimbusCloak", "imgPath": "images/runes/Sorcery/NimbusCloak/NimbusCloak.png"}, "8210": {"name": "Transcendence", "imgPath": "images/runes/Sorcery/Transcendence/Transcendence.png"}, "8234": {"name": "Celerity", "imgPath": "images/runes/Sorcery/Celerity/Celerity.png"}, "8233": {"name": "AbsoluteFocus", "imgPath": "images/runes/Sorcery/AbsoluteFocus/AbsoluteFocus.png"}, "8237": {"name": "Scorch", "imgPath": "images/runes/Sorcery/Scorch/Scorch.png"}, "8232": {"name": "Waterwalking", "imgPath": "images/runes/Sorcery/Waterwalking/Waterwalking.png"}, "8236": {"name": "GatheringStorm", "imgPath": "images/runes/Sorcery/GatheringStorm/GatheringStorm.png"}}
itemList = {"1001": {"name": "Boots of Speed", "imgPath": "images/item/1001.png"}, "1004": {"name": "Faerie Charm", "imgPath": "images/item/1004.png"}, "1006": {"name": "Rejuvenation Bead", "imgPath": "images/item/1006.png"}, "1011": {"name": "Giant's Belt", "imgPath": "images/item/1011.png"}, "1018": {"name": "Cloak of Agility", "imgPath": "images/item/1018.png"}, "1026": {"name": "Blasting Wand", "imgPath": "images/item/1026.png"}, "1027": {"name": "Sapphire Crystal", "imgPath": "images/item/1027.png"}, "1028": {"name": "Ruby Crystal", "imgPath": "images/item/1028.png"}, "1029": {"name": "Cloth Armor", "imgPath": "images/item/1029.png"}, "1031": {"name": "Chain Vest", "imgPath": "images/item/1031.png"}, "1033": {"name": "Null-Magic Mantle", "imgPath": "images/item/1033.png"}, "1036": {"name": "Long Sword", "imgPath": "images/item/1036.png"}, "1037": {"name": "Pickaxe", "imgPath": "images/item/1037.png"}, "1038": {"name": "B. F. Sword", "imgPath": "images/item/1038.png"}, "1039": {"name": "Hunter's Talisman", "imgPath": "images/item/1039.png"}, "1041": {"name": "Hunter's Machete", "imgPath": "images/item/1041.png"}, "1042": {"name": "Dagger", "imgPath": "images/item/1042.png"}, "1043": {"name": "Recurve Bow", "imgPath": "images/item/1043.png"}, "1052": {"name": "Amplifying Tome", "imgPath": "images/item/1052.png"}, "1053": {"name": "Vampiric Scepter", "imgPath": "images/item/1053.png"}, "1054": {"name": "Doran's Shield", "imgPath": "images/item/1054.png"}, "1055": {"name": "Doran's Blade", "imgPath": "images/item/1055.png"}, "1056": {"name": "Doran's Ring", "imgPath": "images/item/1056.png"}, "1057": {"name": "Negatron Cloak", "imgPath": "images/item/1057.png"}, "1058": {"name": "Needlessly Large Rod", "imgPath": "images/item/1058.png"}, "1082": {"name": "Dark Seal", "imgPath": "images/item/1082.png"}, "1083": {"name": "Cull", "imgPath": "images/item/1083.png"}, "1400": {"name": "Enchantment: Warrior", "imgPath": "images/item/1400.png"}, "1401": {"name": "Enchantment: Cinderhulk", "imgPath": "images/item/1401.png"}, "1402": {"name": "Enchantment: Runic Echoes", "imgPath": "images/item/1402.png"}, "1412": {"name": "Enchantment: Warrior", "imgPath": "images/item/1412.png"}, "1413": {"name": "Enchantment: Cinderhulk", "imgPath": "images/item/1413.png"}, "1414": {"name": "Enchantment: Runic Echoes", "imgPath": "images/item/1414.png"}, "1416": {"name": "Enchantment: Bloodrazor", "imgPath": "images/item/1416.png"}, "1419": {"name": "Enchantment: Bloodrazor", "imgPath": "images/item/1419.png"}, "2003": {"name": "Health Potion", "imgPath": "images/item/2003.png"}, "2006": {"name": "Showdown Health Potion", "imgPath": "images/item/2006.png"}, "2009": {"name": "Total Biscuit of Rejuvenation", "imgPath": "images/item/2009.png"}, "2010": {"name": "Total Biscuit of Everlasting Will", "imgPath": "images/item/2010.png"}, "2015": {"name": "Kircheis Shard", "imgPath": "images/item/2015.png"}, "2031": {"name": "Refillable Potion", "imgPath": "images/item/2031.png"}, "2033": {"name": "Corrupting Potion", "imgPath": "images/item/2033.png"}, "2047": {"name": "Oracle's Extract", "imgPath": "images/item/2047.png"}, "2051": {"name": "Guardian's Horn", "imgPath": "images/item/2051.png"}, "2052": {"name": "Poro-Snax", "imgPath": "images/item/2052.png"}, "2054": {"name": "Diet Poro-Snax", "imgPath": "images/item/2054.png"}, "2055": {"name": "Control Ward", "imgPath": "images/item/2055.png"}, "2065": {"name": "Shurelya's Reverie", "imgPath": "images/item/2065.png"}, "2138": {"name": "Elixir of Iron", "imgPath": "images/item/2138.png"}, "2139": {"name": "Elixir of Sorcery", "imgPath": "images/item/2139.png"}, "2140": {"name": "Elixir of Wrath", "imgPath": "images/item/2140.png"}, "2403": {"name": "Minion Dematerializer", "imgPath": "images/item/2403.png"}, "2419": {"name": "Commencing Stopwatch", "imgPath": "images/item/2419.png"}, "2420": {"name": "Stopwatch", "imgPath": "images/item/2420.png"}, "2421": {"name": "Broken Stopwatch", "imgPath": "images/item/2421.png"}, "2422": {"name": "Slightly Magical Boots", "imgPath": "images/item/2422.png"}, "2423": {"name": "Stopwatch", "imgPath": "images/item/2423.png"}, "2424": {"name": "Broken Stopwatch", "imgPath": "images/item/2424.png"}, "3001": {"name": "Abyssal Mask", "imgPath": "images/item/3001.png"}, "3003": {"name": "Archangel's Staff", "imgPath": "images/item/3003.png"}, "3004": {"name": "Manamune", "imgPath": "images/item/3004.png"}, "3006": {"name": "Berserker's Greaves", "imgPath": "images/item/3006.png"}, "3007": {"name": "Archangel's Staff (Quick Charge)", "imgPath": "images/item/3007.png"}, "3008": {"name": "Manamune (Quick Charge)", "imgPath": "images/item/3008.png"}, "3009": {"name": "Boots of Swiftness", "imgPath": "images/item/3009.png"}, "3010": {"name": "Catalyst of Aeons", "imgPath": "images/item/3010.png"}, "3020": {"name": "Sorcerer's Shoes", "imgPath": "images/item/3020.png"}, "3022": {"name": "Frozen Mallet", "imgPath": "images/item/3022.png"}, "3024": {"name": "Glacial Shroud", "imgPath": "images/item/3024.png"}, "3025": {"name": "Iceborn Gauntlet", "imgPath": "images/item/3025.png"}, "3026": {"name": "Guardian Angel", "imgPath": "images/item/3026.png"}, "3027": {"name": "Rod of Ages", "imgPath": "images/item/3027.png"}, "3028": {"name": "Chalice of Harmony", "imgPath": "images/item/3028.png"}, "3029": {"name": "Rod of Ages (Quick Charge)", "imgPath": "images/item/3029.png"}, "3030": {"name": "Hextech GLP-800", "imgPath": "images/item/3030.png"}, "3031": {"name": "Infinity Edge", "imgPath": "images/item/3031.png"}, "3033": {"name": "Mortal Reminder", "imgPath": "images/item/3033.png"}, "3035": {"name": "Last Whisper", "imgPath": "images/item/3035.png"}, "3036": {"name": "Lord Dominik's Regards", "imgPath": "images/item/3036.png"}, "3040": {"name": "Seraph's Embrace", "imgPath": "images/item/3040.png"}, "3041": {"name": "Mejai's Soulstealer", "imgPath": "images/item/3041.png"}, "3042": {"name": "Muramana", "imgPath": "images/item/3042.png"}, "3043": {"name": "Muramana", "imgPath": "images/item/3043.png"}, "3044": {"name": "Phage", "imgPath": "images/item/3044.png"}, "3046": {"name": "Phantom Dancer", "imgPath": "images/item/3046.png"}, "3047": {"name": "Ninja Tabi", "imgPath": "images/item/3047.png"}, "3048": {"name": "Seraph's Embrace", "imgPath": "images/item/3048.png"}, "3050": {"name": "Zeke's Convergence", "imgPath": "images/item/3050.png"}, "3052": {"name": "Jaurim's Fist", "imgPath": "images/item/3052.png"}, "3053": {"name": "Sterak's Gage", "imgPath": "images/item/3053.png"}, "3057": {"name": "Sheen", "imgPath": "images/item/3057.png"}, "3065": {"name": "Spirit Visage", "imgPath": "images/item/3065.png"}, "3067": {"name": "Kindlegem", "imgPath": "images/item/3067.png"}, "3068": {"name": "Sunfire Cape", "imgPath": "images/item/3068.png"}, "3070": {"name": "Tear of the Goddess", "imgPath": "images/item/3070.png"}, "3071": {"name": "Black Cleaver", "imgPath": "images/item/3071.png"}, "3072": {"name": "Bloodthirster", "imgPath": "images/item/3072.png"}, "3073": {"name": "Tear of the Goddess (Quick Charge)", "imgPath": "images/item/3073.png"}, "3074": {"name": "Ravenous Hydra", "imgPath": "images/item/3074.png"}, "3075": {"name": "Thornmail", "imgPath": "images/item/3075.png"}, "3076": {"name": "Bramble Vest", "imgPath": "images/item/3076.png"}, "3077": {"name": "Tiamat", "imgPath": "images/item/3077.png"}, "3078": {"name": "Trinity Force", "imgPath": "images/item/3078.png"}, "3082": {"name": "Warden's Mail", "imgPath": "images/item/3082.png"}, "3083": {"name": "Warmog's Armor", "imgPath": "images/item/3083.png"}, "3084": {"name": "Overlord's Bloodmail", "imgPath": "images/item/3084.png"}, "3085": {"name": "Runaan's Hurricane", "imgPath": "images/item/3085.png"}, "3086": {"name": "Zeal", "imgPath": "images/item/3086.png"}, "3087": {"name": "Statikk Shiv", "imgPath": "images/item/3087.png"}, "3089": {"name": "Rabadon's Deathcap", "imgPath": "images/item/3089.png"}, "3091": {"name": "Wit's End", "imgPath": "images/item/3091.png"}, "3094": {"name": "Rapid Firecannon", "imgPath": "images/item/3094.png"}, "3095": {"name": "Stormrazor", "imgPath": "images/item/3095.png"}, "3100": {"name": "Lich Bane", "imgPath": "images/item/3100.png"}, "3101": {"name": "Stinger", "imgPath": "images/item/3101.png"}, "3102": {"name": "Banshee's Veil", "imgPath": "images/item/3102.png"}, "3105": {"name": "Aegis of the Legion", "imgPath": "images/item/3105.png"}, "3107": {"name": "Redemption", "imgPath": "images/item/3107.png"}, "3108": {"name": "Fiendish Codex", "imgPath": "images/item/3108.png"}, "3109": {"name": "Knight's Vow", "imgPath": "images/item/3109.png"}, "3110": {"name": "Frozen Heart", "imgPath": "images/item/3110.png"}, "3111": {"name": "Mercury's Treads", "imgPath": "images/item/3111.png"}, "3112": {"name": "Guardian's Orb", "imgPath": "images/item/3112.png"}, "3113": {"name": "Aether Wisp", "imgPath": "images/item/3113.png"}, "3114": {"name": "Forbidden Idol", "imgPath": "images/item/3114.png"}, "3115": {"name": "Nashor's Tooth", "imgPath": "images/item/3115.png"}, "3116": {"name": "Rylai's Crystal Scepter", "imgPath": "images/item/3116.png"}, "3117": {"name": "Boots of Mobility", "imgPath": "images/item/3117.png"}, "3123": {"name": "Executioner's Calling", "imgPath": "images/item/3123.png"}, "3124": {"name": "Guinsoo's Rageblade", "imgPath": "images/item/3124.png"}, "3133": {"name": "Caulfield's Warhammer", "imgPath": "images/item/3133.png"}, "3134": {"name": "Serrated Dirk", "imgPath": "images/item/3134.png"}, "3135": {"name": "Void Staff", "imgPath": "images/item/3135.png"}, "3136": {"name": "Haunting Guise", "imgPath": "images/item/3136.png"}, "3137": {"name": "Dervish Blade", "imgPath": "images/item/3137.png"}, "3139": {"name": "Mercurial Scimitar", "imgPath": "images/item/3139.png"}, "3140": {"name": "Quicksilver Sash", "imgPath": "images/item/3140.png"}, "3142": {"name": "Youmuu's Ghostblade", "imgPath": "images/item/3142.png"}, "3143": {"name": "Randuin's Omen", "imgPath": "images/item/3143.png"}, "3144": {"name": "Bilgewater Cutlass", "imgPath": "images/item/3144.png"}, "3145": {"name": "Hextech Revolver", "imgPath": "images/item/3145.png"}, "3146": {"name": "Hextech Gunblade", "imgPath": "images/item/3146.png"}, "3147": {"name": "Duskblade of Draktharr", "imgPath": "images/item/3147.png"}, "3151": {"name": "Liandry's Torment", "imgPath": "images/item/3151.png"}, "3152": {"name": "Hextech Protobelt-01", "imgPath": "images/item/3152.png"}, "3153": {"name": "Blade of the Ruined King", "imgPath": "images/item/3153.png"}, "3155": {"name": "Hexdrinker", "imgPath": "images/item/3155.png"}, "3156": {"name": "Maw of Malmortius", "imgPath": "images/item/3156.png"}, "3157": {"name": "Zhonya's Hourglass", "imgPath": "images/item/3157.png"}, "3158": {"name": "Ionian Boots of Lucidity", "imgPath": "images/item/3158.png"}, "3161": {"name": "Spear of Shojin", "imgPath": "images/item/3161.png"}, "3165": {"name": "Morellonomicon", "imgPath": "images/item/3165.png"}, "3174": {"name": "Athene's Unholy Grail", "imgPath": "images/item/3174.png"}, "3175": {"name": "Head of Kha'Zix", "imgPath": "images/item/3175.png"}, "3179": {"name": "Umbral Glaive", "imgPath": "images/item/3179.png"}, "3181": {"name": "Sanguine Blade", "imgPath": "images/item/3181.png"}, "3184": {"name": "Guardian's Hammer", "imgPath": "images/item/3184.png"}, "3190": {"name": "Locket of the Iron Solari", "imgPath": "images/item/3190.png"}, "3191": {"name": "Seeker's Armguard", "imgPath": "images/item/3191.png"}, "3193": {"name": "Gargoyle Stoneplate", "imgPath": "images/item/3193.png"}, "3194": {"name": "Adaptive Helm", "imgPath": "images/item/3194.png"}, "3196": {"name": "Hex Core mk-1", "imgPath": "images/item/3196.png"}, "3197": {"name": "Hex Core mk-2", "imgPath": "images/item/3197.png"}, "3198": {"name": "Perfect Hex Core", "imgPath": "images/item/3198.png"}, "3200": {"name": "Prototype Hex Core", "imgPath": "images/item/3200.png"}, "3211": {"name": "Spectre's Cowl", "imgPath": "images/item/3211.png"}, "3222": {"name": "Mikael's Crucible", "imgPath": "images/item/3222.png"}, "3285": {"name": "Luden's Echo", "imgPath": "images/item/3285.png"}, "3340": {"name": "Warding Totem (Trinket)", "imgPath": "images/item/3340.png"}, "3348": {"name": "Arcane Sweeper", "imgPath": "images/item/3348.png"}, "3361": {"name": "Greater Stealth Totem (Trinket)", "imgPath": "images/item/3361.png"}, "3362": {"name": "Greater Vision Totem (Trinket)", "imgPath": "images/item/3362.png"}, "3363": {"name": "Farsight Alteration", "imgPath": "images/item/3363.png"}, "3364": {"name": "Oracle Lens", "imgPath": "images/item/3364.png"}, "3371": {"name": "Molten Edge", "imgPath": "images/item/3371.png"}, "3373": {"name": "Forgefire Cape", "imgPath": "images/item/3373.png"}, "3374": {"name": "Rabadon's Deathcrown", "imgPath": "images/item/3374.png"}, "3379": {"name": "Infernal Mask", "imgPath": "images/item/3379.png"}, "3380": {"name": "Obsidian Cleaver", "imgPath": "images/item/3380.png"}, "3382": {"name": "Salvation", "imgPath": "images/item/3382.png"}, "3383": {"name": "Circlet of the Iron Solari", "imgPath": "images/item/3383.png"}, "3384": {"name": "Trinity Fusion", "imgPath": "images/item/3384.png"}, "3386": {"name": "Zhonya's Paradox", "imgPath": "images/item/3386.png"}, "3387": {"name": "Frozen Fist", "imgPath": "images/item/3387.png"}, "3388": {"name": "Youmuu's Wraithblade", "imgPath": "images/item/3388.png"}, "3389": {"name": "Might of the Ruined King", "imgPath": "images/item/3389.png"}, "3390": {"name": "Luden's Pulse", "imgPath": "images/item/3390.png"}, "3400": {"name": "'Your Cut'", "imgPath": "images/item/3400.png"}, "3410": {"name": "Head of Kha'Zix", "imgPath": "images/item/3410.png"}, "3416": {"name": "Head of Kha'Zix", "imgPath": "images/item/3416.png"}, "3422": {"name": "Head of Kha'Zix", "imgPath": "images/item/3422.png"}, "3455": {"name": "Head of Kha'Zix", "imgPath": "images/item/3455.png"}, "3504": {"name": "Ardent Censer", "imgPath": "images/item/3504.png"}, "3508": {"name": "Essence Reaver", "imgPath": "images/item/3508.png"}, "3513": {"name": "Eye of the Herald", "imgPath": "images/item/3513.png"}, "3514": {"name": "Eye of the Herald", "imgPath": "images/item/3514.png"}, "3520": {"name": "Ghost Poro", "imgPath": "images/item/3520.png"}, "3599": {"name": "Black Spear", "imgPath": "images/item/3599.png"}, "3600": {"name": "Black Spear", "imgPath": "images/item/3600.png"}, "3671": {"name": "Enchantment: Warrior", "imgPath": "images/item/3671.png"}, "3672": {"name": "Enchantment: Cinderhulk", "imgPath": "images/item/3672.png"}, "3673": {"name": "Enchantment: Runic Echoes", "imgPath": "images/item/3673.png"}, "3675": {"name": "Enchantment: Bloodrazor", "imgPath": "images/item/3675.png"}, "3680": {"name": "Frosted Snax", "imgPath": "images/item/3680.png"}, "3681": {"name": "Super Spicy Snax", "imgPath": "images/item/3681.png"}, "3682": {"name": "Espresso Snax", "imgPath": "images/item/3682.png"}, "3683": {"name": "Rainbow Snax Party Pack!", "imgPath": "images/item/3683.png"}, "3684": {"name": "Dawnbringer Snax", "imgPath": "images/item/3684.png"}, "3685": {"name": "Nightbringer Snax", "imgPath": "images/item/3685.png"}, "3690": {"name": "Cosmic Shackle", "imgPath": "images/item/3690.png"}, "3691": {"name": "Singularity Lantern", "imgPath": "images/item/3691.png"}, "3692": {"name": "Dark Matter Scythe", "imgPath": "images/item/3692.png"}, "3693": {"name": "Gravity Boots", "imgPath": "images/item/3693.png"}, "3694": {"name": "Cloak of Stars", "imgPath": "images/item/3694.png"}, "3695": {"name": "Dark Star Sigil", "imgPath": "images/item/3695.png"}, "3706": {"name": "Stalker's Blade", "imgPath": "images/item/3706.png"}, "3715": {"name": "Skirmisher's Sabre", "imgPath": "images/item/3715.png"}, "3742": {"name": "Dead Man's Plate", "imgPath": "images/item/3742.png"}, "3748": {"name": "Titanic Hydra", "imgPath": "images/item/3748.png"}, "3751": {"name": "Bami's Cinder", "imgPath": "images/item/3751.png"}, "3800": {"name": "Righteous Glory", "imgPath": "images/item/3800.png"}, "3801": {"name": "Crystalline Bracer", "imgPath": "images/item/3801.png"}, "3802": {"name": "Lost Chapter", "imgPath": "images/item/3802.png"}, "3812": {"name": "Death's Dance", "imgPath": "images/item/3812.png"}, "3814": {"name": "Edge of Night", "imgPath": "images/item/3814.png"}, "3850": {"name": "Spellthief's Edge", "imgPath": "images/item/3850.png"}, "3851": {"name": "Frostfang", "imgPath": "images/item/3851.png"}, "3853": {"name": "Shard of True Ice", "imgPath": "images/item/3853.png"}, "3854": {"name": "Steel Shoulderguards", "imgPath": "images/item/3854.png"}, "3855": {"name": "Runesteel Spaulders", "imgPath": "images/item/3855.png"}, "3857": {"name": "Pauldrons of Whiterock", "imgPath": "images/item/3857.png"}, "3858": {"name": "Relic Shield", "imgPath": "images/item/3858.png"}, "3859": {"name": "Targon's Buckler", "imgPath": "images/item/3859.png"}, "3860": {"name": "Bulwark of the Mountain", "imgPath": "images/item/3860.png"}, "3862": {"name": "Spectral Sickle", "imgPath": "images/item/3862.png"}, "3863": {"name": "Harrowing Crescent", "imgPath": "images/item/3863.png"}, "3864": {"name": "Black Mist Scythe", "imgPath": "images/item/3864.png"}, "3901": {"name": "Fire at Will", "imgPath": "images/item/3901.png"}, "3902": {"name": "Death's Daughter", "imgPath": "images/item/3902.png"}, "3903": {"name": "Raise Morale", "imgPath": "images/item/3903.png"}, "3905": {"name": "Twin Shadows", "imgPath": "images/item/3905.png"}, "3907": {"name": "Spellbinder", "imgPath": "images/item/3907.png"}, "3916": {"name": "Oblivion Orb", "imgPath": "images/item/3916.png"}}
spellList = {"21": {"name": "Barrier", "imgPath": "images/spells/SummonerBarrier.png"}, "1": {"name": "Cleanse", "imgPath": "images/spells/SummonerBoost.png"}, "14": {"name": "Ignite", "imgPath": "images/spells/SummonerDot.png"}, "3": {"name": "Exhaust", "imgPath": "images/spells/SummonerExhaust.png"}, "4": {"name": "Flash", "imgPath": "images/spells/SummonerFlash.png"}, "6": {"name": "Ghost", "imgPath": "images/spells/SummonerHaste.png"}, "7": {"name": "Heal", "imgPath": "images/spells/SummonerHeal.png"}, "SummonerMana": {"name": "Clarity", "imgPath": "images/spells/SummonerMana.png"}, "SummonerPoroRecall": {"name": "To the King!", "imgPath": "images/spells/SummonerPoroRecall.png"}, "SummonerPoroThrow": {"name": "Poro Toss", "imgPath": "images/spells/SummonerPoroThrow.png"}, "11": {"name": "Smite", "imgPath": "images/spells/SummonerSmite.png"}, "SummonerSnowURFSnowball_Mark": {"name": "Mark", "imgPath": "images/spells/SummonerSnowURFSnowball_Mark.png"}, "32": {"name": "Mark", "imgPath": "images/spells/SummonerSnowball.png"}, "12": {"name": "Teleport", "imgPath": "images/spells/SummonerTeleport.png"}}

def useAPI():
    for item in SUMMONERS:
        accountId = getId(item['name'])
        item['id'] = accountId
        history = getHistory(accountId)
        item['history'] = history
        matchInfo = getMatch(history, accountId)
        item['matchInfo'] = matchInfo
 

try:
    useAPI()
except Exception as ex:
    print("Exception: " + str(ex))


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

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

response_object = {'status': 'success', 'message':''}
@app.route('/summoners', methods=['GET', 'POST'])
def all_summoners():
    if request.method == 'POST':
        post_data = request.get_json()
        accId = getId(post_data.get('name'))
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
                    'name': post_data.get('name'),
                    'history': history,
                    'matchInfo': getMatch(history, accId),
                    'startIndex': 0,
                    'endIndex': 10,
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


def replace_summoner(summoner_id, post_data):
    remove_summoner(summoner_id)
    accId = getId(post_data.get('name'))
    history = getHistory(accId)
    SUMMONERS.append({
        'id': accId,
        'name': post_data.get('name'),
        'history': history,
        'matchInfo': getMatch(history, accId),
        'startIndex': 0,
        'endIndex': 10,
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
