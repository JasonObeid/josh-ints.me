import json

def mapIds():
    champMap = {}
    with open('./champion.json') as file:
        x = file.read()
        x = json.loads(x)
        championList = x['data']
        for champ in championList:
            champKey = x['data'][champ]['key']
            champMap[champKey] = champ
    #print(champMap)
    with open('../dataDragon/champIds.json', 'w') as json_file:
        json.dump(champMap, json_file)


mapIds()