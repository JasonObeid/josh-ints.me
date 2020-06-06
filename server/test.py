from collections import Counter
import csv
import json
from statistics import mean, mode

def getSpells(spellIds):
    spells = {}
    spells['spell1'] = spellIds[0][0]
    spells['spell2'] = spellIds[1][0]
    return spells

def getItems(itemIds, trinketId):
    items = {}
    itemsList = []
    print(itemIds)
    if trinketId != 0:
        trinketName = itemList[str(trinketId)]
    else:
        trinketName = ''
    for item in itemIds:
        if(item != 0):
            name = itemList[str(item)]
            itemsList.append(name)
    items['itemsList'] = itemsList
    items['count'] = len(itemsList)  # not including trinket
    items['trinket'] = trinketName
    return items


def getRunes(topPrimary, topSecondary):
    runes = {}
    print(topPrimary, topSecondary)
    for optionPrimary, optionSecondary, i in zip(topPrimary, topSecondary, range(len(topPrimary))):
        optionPrimary = optionPrimary[0]
        optionSecondary = optionSecondary[0]
        option = {}
        keystoneId = '8112'#str(optionPrimary[0])
        keystone = runeList[keystoneId]
        primary1Id = str(optionPrimary[1])
        primary1 = runeList[primary1Id]
        primary2Id = str(optionPrimary[2])
        primary2 = runeList[primary2Id]
        primary3Id = str(optionPrimary[3])
        primary3 = runeList[primary3Id]
        secondary0Id = '8345' # str(optionSecondary[0])
        secondary0 = runeList[secondary0Id]
        secondary1Id = str(optionSecondary[1])
        secondary1 = runeList[secondary1Id]
        for key, value in branchList.items():
            if keystoneId[:2] in key:
                primaryBranchName = value
            if secondary0Id[:2] in key:
                secondaryBranchName = value
        primaryBranch = {'keystone': keystone, 'perk1': primary1, 'perk2': primary2, 'perk3': primary3,
                        'name': primaryBranchName['name'], 'imgPath': primaryBranchName['imgPath']}
        secondaryBranch = {'perk0': secondary0, 'perk1': secondary1,
                        'name': secondaryBranchName['name'], 'imgPath': secondaryBranchName['imgPath']}
        option['primaryBranch'] = primaryBranch
        option['secondaryBranch'] = secondaryBranch
        runes[i] = option
    return runes

with open('../dataDragon/champIds.json') as file1:
    champList = json.load(file1)
with open('../dataDragon/branchIds.json') as file3:
    branchList = json.load(file3)
with open('../dataDragon/runeIds.json') as file4:
    runeList = json.load(file4)
with open('../dataDragon/itemIds.json') as file5:
    itemList = json.load(file5)

with open('./entries_2.csv', mode='r', newline='') as statsFile:
    reader = csv.reader(statsFile, delimiter=',')
    rows = [line for line in reader]

with open('./stats.json', 'w') as json_file:
    champDict = {}
    for champId in champList.keys():
        kills = []
        assists = []
        deaths = []
        wins = 0
        cs = []
        primary = []
        secondary = []
        items = []
        trinket = []
        spells = []
        for row in rows:
            if row[0] == champId:
                if row[5] == 'True':
                    wins += 1
                kills.append(int(row[1]))
                assists.append(int(row[2]))
                deaths.append(int(row[3]))
                cs.append(int(row[4]))
                primaries = tuple(int(x) for x in row[6:10])
                primary.append(primaries)
                secondaries = tuple(int(x) for x in row[11:13])
                secondary.append(secondaries)
                item = tuple(int(x) for x in row[14:19])
                items.append(item)
                trinket.append(int(row[20]))
                summSpells = tuple(int(x) for x in row[21:])
                spells.append(summSpells[0])
                spells.append(summSpells[1])
        if len(kills) > 0:
            topPrimary = Counter(primary).most_common(2)
            topSecondary = Counter(secondary).most_common(2)
            topSpells = Counter(spells).most_common(2)
            stats = {'kills': mean(kills), 'deaths': mean(deaths), 'cs': mean(cs), 'wins':f'{round((wins/len(kills)*100),1)}%'}
            runes = getRunes(topPrimary, topSecondary)
            items = getItems(mode(items),  mode(trinket))
            spells = getSpells(topSpells)
            champDict[champId] = {'samples': len(kills), 'stats':stats,
                     'items': items, 'runes': runes, 'spells': spells}
    print(champDict)
    json.dump(champDict, json_file, indent=3)