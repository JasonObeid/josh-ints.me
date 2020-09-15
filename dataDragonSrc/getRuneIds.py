import json

def mapIds():
    ShardDict = {
            '5008': {'name':'Adaptive Force', 'imgPath': "images/shards/5008.png"},
            '5002': {'name':'Armour', 'imgPath': "images/shards/5002.png"},
            '5005': {'name':'Attack Speed', 'imgPath': "images/shards/5005.png"},
            '5007': {'name':'Cooldown Reduction', 'imgPath': "images/shards/5007.png"},
            '5001': {'name':'Health', 'imgPath': "images/shards/5001.png"},
            '5003': {'name':'Magic Resist', 'imgPath': "images/shards/5003.png"}
        }
    runeDict = {}
    with open('runesReforged.json') as file:
        x = file.read()
        runeList = json.loads(x)
        branchDict = {}
        for branch in runeList:
            branchList = branch['slots']
            branchName = branch['key']
            branchId = branch['id']
            branchImgPath = "images/runes/" + branchName + '.png'
            branchDict[branchId] = {'name': branchName, 'imgPath': branchImgPath}
            for x in branchList:
                runeList = x['runes']
                for y in runeList:
                    runeId = y['id']
                    runeName = y['key']
                    imgPath = "images/runes/" + branchName + '/' + runeName + '/' + runeName + '.png'
                    runeDict[runeId] = {'name': runeName, 'imgPath': imgPath}
            #print(runeDict)
        #print(branchDict)
    with open('../src/api/dataDragon/runeIds.json', 'w') as json_file1:
        json.dump(runeDict, json_file1)
    with open('../src/api/dataDragon/branchIds.json', 'w') as json_file2:
        json.dump(branchDict, json_file2)
    with open('../src/api/dataDragon/shardIds.json', 'w') as json_file3:
        json.dump(ShardDict, json_file3)
        
mapIds()