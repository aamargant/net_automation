import requests
import json
from tabulate import tabulate
import sys
import nodes
import xml.etree.ElementTree as ET
import check_input_node as check_node


def get_request(node):
  url = "https://" + node["address"] + "/restconf/data/Cisco-NX-OS-device:System"
  
  payload= open("ip_routing_conf.json").read()
  headers = {
    'Content-Type': 'application/yang.data+json',
    'Accept': 'application/yang.data+json',  
  }

  response = requests.request("PATCH", url, auth=('cisco', 'cisco'), headers=headers, data=payload,  verify=False) 


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