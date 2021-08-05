import json

# rawName 【白いツバサ】櫻木 真乃
# returns (【白いツバサ】櫻木 真乃, 櫻木 真乃)
def processName(rawName):
    # ["【白いツバサ", "櫻木 真乃"]
    tmpSplit = rawName.split("】")

    idolName = "".join(tmpSplit[1].split(" "))
    cardName = "】".join([tmpSplit[0], idolName])
    return (idolName, cardName)

with open('./idol/idol-info.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    idolDict = {}
    for card in data:
        (idolName, cardName) = processName(card['name'])

        idolDict.setdefault(idolName, {
            "ids": [],
            "details": {}
        })
        cardId = card['id']

        idolDict[idolName]['details'][cardId] = card
        idolDict[idolName]['details'][cardId]['name'] = cardName
        idolDict[idolName]['ids'].append((cardId, cardName))
    for idolName in idolDict:
        idolDict[idolName]['ids'] = sorted(idolDict[idolName]['ids'], key=lambda x: int(x[0]))
        with open("./idol/%s.json"%idolName,"w", encoding="utf8") as idolF:
            json.dump(idolDict[idolName],idolF,ensure_ascii=False,indent=2,separators=(',',':'), sort_keys=True, )
    

