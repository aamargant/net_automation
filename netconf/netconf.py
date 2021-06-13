from ncclient import manager
import xmltodict
from tabulate import tabulate
import nodes
import sys
import re

def get_request(xmlstring): 
    with manager.connect(host=node["address"], port=node["port"], 
        username= node["username"], password=node["password"],
        hostkey_verify=False) as device:

        netconf_reply = device.get(('subtree', xmlstring))


    print("")
    print("")
    node_object = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    node_interfaces = node_object["interfaces"]["interface"]

    headers = ["Interface", "Description", "Enabled", "IP / Mode", "Broadcast(IN)", "Unicast(IN)", "Multicast(IN)", "Broadcast(OUT)", "Unicast(OUT)", "Multicast(OUT)"]

    table = [] 

    print(" " + node["name"] + " (" + node_interfaces[0]["ethernet"]["state"].get("mac-address") + ")")
    for idx, interface in enumerate(node_interfaces):
         config = interface["config"]
         
         if "description" in config:
            ip_config = interface["subinterfaces"]["subinterface"]
            inside_table = []
            table.append(inside_table)
            table[idx].append(interface["name"])
            table[idx].append(config["description"])
            table[idx].append(config["enabled"])

            if "ipv4" in ip_config:
                table[idx].append(ip_config["ipv4"]["addresses"]["address"]["config"].get("ip"))
            elif "switched-vlan" in interface["ethernet"]:
                table[idx].append(interface["ethernet"]["switched-vlan"]["state"]["interface-mode"])

            table[idx].append(interface["state"]["counters"].get("in-broadcast-pkts"))
            table[idx].append(interface["state"]["counters"].get("in-unicast-pkts"))
            table[idx].append(interface["state"]["counters"].get("in-multicast-pkts"))
            table[idx].append(interface["state"]["counters"].get("out-broadcast-pkts"))
            table[idx].append(interface["state"]["counters"].get("out-unicast-pkts"))
            table[idx].append(interface["state"]["counters"].get("out-multicast-pkts"))

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

xml_filter = open("filter.xml").read()

if isinstance(node, list):
    node_list = node
    for n in node_list:
        node = n
        get_request(xml_filter)
else:
    get_request(xml_filter)

