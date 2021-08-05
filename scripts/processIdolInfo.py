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
            "list": [],
            "details": {}
        })
        cardId = card['id']

        idolDict[idolName]['details'][cardId] = card
        idolDict[idolName]['details'][cardId]['name'] = cardName
        idolDict[idolName]['list'].append({
            "id": cardId,
            "name": cardName
        })
    for idolName in idolDict:
        idolDict[idolName]['list'] = sorted(
            idolDict[idolName]['list'], key=lambda x: int(x["id"]))
        with open("./idol/%s.json" % idolName, "w", encoding="utf8") as idolF:
            json.dump(idolDict[idolName], idolF, ensure_ascii=False,
                      indent=2, separators=(',', ':'), sort_keys=True, )
