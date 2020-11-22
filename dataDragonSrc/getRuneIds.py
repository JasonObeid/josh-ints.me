import json

def mapIds():
    """ShardDict = {
        {'id':'5008', 'name':'Adaptive Force', 'imgPath': "images/shards/5008.png"},
        {'id':'5002', 'name':'Armour', 'imgPath': "images/shards/5002.png"},
        {'id':'5005', 'name':'Attack Speed', 'imgPath': "images/shards/5005.png"},
        {'id':'5007', 'name':'Cooldown Reduction', 'imgPath': "images/shards/5007.png"},
        {'id':'5001', 'name':'Health', 'imgPath': "images/shards/5001.png"},
        {'id':'5003', 'name':'Magic Resist', 'imgPath': "images/shards/5003.png"}
    }"""
    
    ShardDict = [
        [{'id':'5008', 'name':'Adaptive Force', 'imgPath': "images/shards/5008.png"},
        {'id':'5005', 'name':'Attack Speed', 'imgPath': "images/shards/5005.png"},
        {'id':'5007', 'name':'Cooldown Reduction', 'imgPath': "images/shards/5007.png"}],

        [{'id':'5008', 'name':'Adaptive Force', 'imgPath': "images/shards/5008.png"},
        {'id':'5002', 'name':'Armour', 'imgPath': "images/shards/5002.png"},
        {'id':'5003', 'name':'Magic Resist', 'imgPath': "images/shards/5003.png"}],

        [{'id':'5001', 'name':'Health', 'imgPath': "images/shards/5001.png"},
        {'id':'5002', 'name':'Armour', 'imgPath': "images/shards/5002.png"},
        {'id':'5003', 'name':'Magic Resist', 'imgPath': "images/shards/5003.png"}]
    ]

    runeDict = {}
    with open('runesReforged.json') as file:
        x = file.read()
        runes = json.loads(x)
        branchDict = {}

        #make rune dictionary
        for branch in runes:
            branchList = branch['slots']
            branchName = branch['key']
            branchId = branch['id']
            branchImgPath = f"images/{branch['icon']}"
            branchDict[branchId] = {'name': branchName, 'imgPath': branchImgPath}
            for runeRow in branchList:
                runeList = runeRow['runes']
                for rune in runeList:
                    runeId = rune['id']
                    runeName = rune['key']
                    imgPath = f"images/{rune['icon']}"
                    runeDict[runeId] = {'name': runeName, 'imgPath': imgPath}
        
        #make rune 'trees'
        branchDict2 = {}
        for branch in runes:
            branchList = branch['slots']
            branchName = branch['key']
            branchId = branch['id']
            branchImgPath = f"images/{branch['icon']}"
            runeRowList = []
            for runeRow in branchList:
                runeList = runeRow['runes']
                runeRowDict = {}
                for rune in runeList:
                    runeId = rune['id']
                    runeName = rune['key']
                    imgPath = f"images/{rune['icon']}"
                    runeRowDict[runeId] = {'name': runeName, 'imgPath': imgPath, 'id': str(runeId)}
                runeRowList.append(runeRowDict)
            branchDict2[branchId] = {'name': branchName, 'imgPath': branchImgPath, 'runeRows': runeRowList}


    with open('../src/api/dataDragon/runeIds.json', 'w') as json_file1:
        json.dump(runeDict, json_file1)
    with open('../src/api/dataDragon/branchIds.json', 'w') as json_file2:
        json.dump(branchDict, json_file2)
    with open('../src/api/dataDragon/shardIds.json', 'w') as json_file3:
        json.dump(ShardDict, json_file3)
    with open('../src/api/dataDragon/runeMap.json', 'w') as json_file5:
        json.dump(branchDict2, json_file5)

mapIds()