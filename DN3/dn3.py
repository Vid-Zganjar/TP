import json


with open('C:/Users/Vid/Desktop/TP VAJE/VAJA/TP/DN3/zacetniData.json', 'r') as fzac:
    zacetniData = json.load(fzac)

with open('C:/Users/Vid/Desktop/TP VAJE/VAJA/TP/DN3/updateData.json', 'r') as fupd:
    updateData = json.load(fupd)


zacetniSlovar = {x["name"]:x for x in zacetniData["persons"]}


for oseba in updateData["persons"]:
    if oseba["name"] in zacetniSlovar.keys():
        zacetniSlovar[oseba["name"]].update(oseba)


with open('C:/Users/Vid/Desktop/TP VAJE/VAJA/TP/DN3/Data.json', 'w') as f:
    json.dump(zacetniData, f, indent=2)