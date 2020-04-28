import json
name2id = {'SummonerFlash' : 4, 'SummonerSmite' : 11, 'SummonerTeleport' : 12, 'SummonerDot' : 14, 'SummonerBarrier' : 21, 'SummonerBoost' : 1, 'SummonerHeal' : 7, 'SummonerHaste' : 6, 'SummonerExhaust' : 3, 'SummonerSnowball' : 32}
#clarity = ?
def mapIds():
    summonerDict = {}
    with open('summoner.json') as file:
        x = file.read()
        summonerList = json.loads(x)
        for summonerId in summonerList['data']:
            name = summonerList['data'][summonerId]['name']
            if(summonerId in name2id):
                summId = name2id[summonerId]
            else:
                summId = summonerId
            #imgPath = str(summonerId)+'.png'
            imgPath = "images/spells/" + summonerList['data'][summonerId]['image']['full']
            summonerDict[summId] = {'name':name,'imgPath':imgPath}
        print(summonerDict)
    with open('../dataDragon/summonerIds.json', 'w') as json_file:
        json.dump(summonerDict, json_file)


mapIds()