from ncclient import manager
import xmltodict
from tabulate import tabulate
import nodes
import sys
import re
import check_input_node as check_node

def get_request(xml_filter, node): 
    with manager.connect(host=node["address"], port=node["port"], 
        username= node["username"], password=node["password"],
        hostkey_verify=False) as device:

        netconf_reply = device.edit_config(xml_filter, target = 'running')

def setup():
    node = check_node.check_input_node(sys)
    xml_filter = open("filter_desc_conf.xml").read()

    if isinstance(node, list):
        node_list = node
        for n in node_list:
            node = n
            get_request(xml_filter, node)
    else:
        get_request(xml_filter, node)

if __name__ == '__main__':
    setup()
