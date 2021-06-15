import requests
import json
from tabulate import tabulate
import sys
import nodes
import xml.etree.ElementTree as ET
import check_input_node as check_node


def get_request(node):
  url = "https://" + node["address"] + "/restconf/data/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list"
  
  payload= ""
  headers = {
    'Content-Type': 'application/yang.data+json',
    'Accept': 'application/yang.data+xml',  
  }

  response = requests.request("GET", url, auth=('cisco', 'cisco'), headers=headers, data=payload,  verify=False) 

  root = ET.fromstring(response.text).find('rt-items')  
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

def setup():
  node = check_node.check_input_node(sys)
  if isinstance(node, list):
      node_list = node
      for n in node_list:
          node = n
          get_request(node)
  else:
      get_request(node)


if __name__ == '__main__':
    setup()