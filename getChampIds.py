import json

def mapIds():
    champMap = {}
    with open('/home/jason/Downloads/10.4.1/data/en_US/champion.json') as file:
        x = file.read()
        x = json.loads(x)
        championList = x['data']
        for champ in championList:
            champKey = x['data'][champ]['key']
            champMap[champKey] = champ
    #print(champMap)
    with open('champIds.json', 'w') as json_file:
        json.dump(champMap, json_file)


mapIds()