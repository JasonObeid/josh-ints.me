import json

def mapIds():
    itemDict = {}
    with open('item.json') as file:
        x = file.read()
        itemList = json.loads(x)
        for itemId in itemList['data']:
            name = itemList['data'][itemId]['name']
            #imgPath = str(itemId)+'.png'
            imgPath = "images/item/" + itemList['data'][itemId]['image']['full']
            itemDict[itemId] = {'name':name,'imgPath':imgPath}
        print(itemDict)
    with open('../dataDragon/itemIds.json', 'w') as json_file:
        json.dump(itemDict, json_file)


mapIds()