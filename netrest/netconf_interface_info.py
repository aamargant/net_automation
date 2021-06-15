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

        netconf_reply = device.get(('subtree', xml_filter))

    node_object = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    node_interfaces = node_object["interfaces"]["interface"]

    headers = ["Interface", "Description", "Enabled", "IP / Mode", "Broadcast(IN)", "Unicast(IN)", "Multicast(IN)", "Broadcast(OUT)", "Unicast(OUT)", "Multicast(OUT)"]

    table = [] 

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

    print("")
    print("NETCONF interface info")
    print("")
    print(" " + node["name"] + " (" + node_interfaces[0]["ethernet"]["state"].get("mac-address") + ")")
    print(tabulate(table, headers, tablefmt="grid"))


def setup():
    node = check_node.check_input_node(sys)
    xml_filter = open("filter_interfaces.xml").read()

    if isinstance(node, list):
        node_list = node
        for n in node_list:
            node = n
            get_request(xml_filter, node)
    else:
        get_request(xml_filter, node)


if __name__ == '__main__':
    setup()

