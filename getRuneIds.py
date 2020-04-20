import json

def mapIds():
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
    with open('runeIds.json', 'w') as json_file:
        json.dump(runeDict, json_file)
    with open('branchIds.json', 'w') as json_file:
        json.dump(branchDict, json_file)

mapIds()