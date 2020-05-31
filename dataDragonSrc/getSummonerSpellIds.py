import json
def mapIds():
    summonerDict = {}
    with open('summoner.json') as file:
        x = file.read()
        summonerList = json.loads(x)
        for summonerSpell, details in summonerList['data'].items():
            idx = details['key']
            name = details['name']
            img = f"{details['image']['full'][:-4]}.jpg"
            imgPath = f"images/spells/{img}"
            summonerDict[idx] = {'name':name,'imgPath':imgPath}
        print(summonerDict)
    with open('../client/api/dataDragon/summonerIds.json', 'w') as json_file:
        json.dump(summonerDict, json_file)


mapIds()