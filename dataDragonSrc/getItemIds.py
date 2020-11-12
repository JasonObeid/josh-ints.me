import json

def mapIds():
    itemDict = {}
    with open('item.json') as file:
        x = file.read()
        itemList = json.loads(x)
        with open('item_old.json') as oldFile:
            y = oldFile.read()
            oldItemList = json.loads(y)
            for itemId in itemList['data']:
                name = itemList['data'][itemId]['name']
                img = f"{itemList['data'][itemId]['image']['full'][:-4]}.jpg"
                imgPath = f"images/item/{img}"
                itemDict[itemId] = {'name':name,'imgPath':imgPath}

            for itemId in oldItemList['data']:
                if itemId not in itemDict.keys()
                    name = oldItemList['data'][itemId]['name']
                    img = f"{oldItemList['data'][itemId]['image']['full'][:-4]}.jpg"
                    imgPath = f"images/item/{img}"
                    itemDict[itemId] = {'name':name,'imgPath':imgPath}

    with open('../src/api/dataDragon/itemIds.json', 'w') as json_file:
        json.dump(itemDict, json_file)


mapIds()