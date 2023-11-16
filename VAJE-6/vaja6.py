
import requests
import json

    # API URL od infure za Ethereum mainnet
def main():
    # definiraj VARIABLE nase skripte
    url_infura="https://mainnet.infura.io/v3/35217251f6fe408abcffb2078845b1ef"
    headers={
            "Constent-Type": "application/json",
        }
    data=getBlock(url_infura,headers)

    print("stevilo transakcij je: ",countTransactions(data))

def getBlock(url_infura, headers):
        # JSON-RPC request payload  (pogledamo dokumentacijo!)
    payload={
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest",True],
        "id": 0
        }
        # Nastavimo headerje za JSON-RPC request
    

    # Pošljemo request (uporabimo requests.post mdetodo)
    response=requests.post(url_infura, data = json.dumps(payload), headers=headers)

    # Error handling. POgledamo če smo dobili pravilen odgovor.
        # ce ni error-ja (status code 200) sprintamo sporocilo in shranimo dobljeno sporocilo v json
    if response.status_code == 200:
        data=response.json()
        print("dobili smo block")
        with open('blockData.json','w') as f:
            json.dump(data, f, indent=4)
        # else, sprintaj sporocilo da nam ni uspelo dobiti zadnji block in dodaj kateri error oz. code-status code smo dobil
    else:
        print("ni ratal. error code: {response.status_code}")
    return data


def countTransactions(data):
    # naredimo kopijo podatkov - .copy() metoda

    kopija=data.copy()

    # definiramo counter
    counter=0

    # Iteriramo čez transakcije in povečujemo counter
    for transaction in data["result"]["transactions"]:
        counter+=1
   
# Izpišemo/sprintamo counter (število transakcij)
    return counter

main()