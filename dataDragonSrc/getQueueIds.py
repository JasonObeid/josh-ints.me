import json


def mapIds():
    queueDict = {}
    with open('queues.json') as file:
        x = file.read()
        queueList = json.loads(x)
        for queue in queueList:
            description = queue['description']
            if description is None:
                description = 'None'
            else:
                startIndex = len(description)-5
                endIndex = len(description)
                if(description[startIndex:endIndex] == 'games'):
                    description = description[0:startIndex-1]
            queueDict[queue['queueId']] = {
                'map': queue['map'], 'description': description}
        print(queueDict)
    with open('../src/api/dataDragon/queueIds.json', 'w') as json_file:
        json.dump(queueDict, json_file)


mapIds()
