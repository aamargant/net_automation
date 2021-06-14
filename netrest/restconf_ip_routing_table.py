import requests
import json
from tabulate import tabulate
import sys
import nodes
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth


def get_request():
  url = "https://" + node["address"] + "/restconf/data/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list"
  payload=""
  headers = {
    'Content-Type': 'application/yang.data+json',
    'Accept': 'application/yang.data+xml',  
  }

  response = requests.request("GET", url, auth=('cisco', 'cisco'), headers=headers, data=payload,  verify=False) 


  root=ET.fromstring(response.text).find('rt-items')  
  table = [] 
  inside_table = []
  num = 0

  for elem in root:
    inside_table = []
    table.append(inside_table)
    table[num].append(elem[0].text)
    inside_table = []
    table.append(inside_table)
    table[num+1].append(elem[0].text)
    for idx, subatt in enumerate(elem[1]):
      if idx%2==0:
        table[num].append(subatt[1].text)
        table[num].append(subatt[0].text)
      else:
        table[num + 1].append(subatt[1].text)
        table[num + 1].append(subatt[0].text)
    num = num + 2

  headers = ["IP", "Next Hop", "Via Interface"]
  print("")
  print("RESTCONF ip routing table:")
  print("")
  print(node["name"])
  print(tabulate(table, headers, tablefmt="grid"))


if len(sys.argv) < 2:
    print("")
    print("Please write after .py the node(s) to extract information from:")
    table_node = [["Groups"], ["Inidivudal"]]
    print("")
    for key in nodes.__dict__.keys():
        if not key.startswith("_"):
            if isinstance(nodes.__dict__.get(key), list):
                table_node[0].append(key)
            else:
                table_node[1].append(key)
    print(tabulate(table_node, tablefmt="grid"))
    exit()

node = ""
node = nodes.__dict__.get(sys.argv[1])

if node is None:
    print("Please write a valid device name.")
    exit()

if isinstance(node, list):
    node_list = node
    for n in node_list:
        node = n
        get_request()
else:
    get_request()