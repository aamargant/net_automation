import requests
import json

baseUrl = "https://10.10.20.161/api/v0"


def login():
    credencials = json.dumps({
        "username": "developer",
        "password": "C1sco12345"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <Bearer Token>'
    }
    token_auth = requests.request("POST", baseUrl + "/authenticate", headers=headers, data=credencials, verify=False)
    token = 'Bearer ' + token_auth.json()
    print(token)
    return token


def createTopologyFromFile(token):
    with open('campusTopology.yaml', 'rb') as payload:
        headers = {'content-type': 'application/json',
                   'Authorization': token
                   }
        print("")
        nom_lab = input("Escriu nom de la topologia: ")
        response = requests.request("POST", baseUrl + "/import?title="+ nom_lab, headers=headers, data=payload,
                                    verify=False)
        if response.text.__contains__("id"):
            return "Success\n" + response.text
        else:
            return "Failed\n" +response.text

print(createTopologyFromFile(login()))
