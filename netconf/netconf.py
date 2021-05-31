from ncclient import manager
import xmltodict
from tabulate import tabulate
import nodes
import sys

if len(sys.argv) < 2:
    print("Please choose a node to extract information from. (core1, core2, core3, core4 or for all cores: core)")
    exit()

node = ""
if sys.argv[1] == "core1":
    node = nodes.core1
elif sys.argv[1] == "core2":
    node = nodes.core2
elif sys.argv[1] == "core3":
    node = nodes.core3
elif sys.argv[1] == "core4":
    node = nodes.core4
elif sys.argv[1] == "core":
    node = nodes.core

def get_request(xmlstring): 
    with manager.connect(host=node["address"], port=node["port"], 
        username= node["username"], password=node["password"], 
        hostkey_verify=False) as device:

        netconf_reply = device.get(('subtree', xmlstring))

    print("NETCONF RESPONSE:" )
    print("")
    node_object = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    node_interfaces = node_object["interfaces"]["interface"]
    
    headers = ["Interface", "Description", "Enabled", "IP", "Broadcast(IN)", "Unicast(IN)", "Multicast(IN)", "Broadcast(OUT)", "Unicast(OUT)", "Multicast(OUT)"]

    table = [] 

    print(node["name"] + "(" + node_interfaces[0]["ethernet"]["state"].get("mac-address") + ")")
    for idx, interface in enumerate(node_interfaces):
         inside_table = []
         table.append(inside_table)
         table[idx].append(interface["name"])
         table[idx].append(interface["config"]["description"])
         table[idx].append(interface["config"]["enabled"])
         table[idx].append(interface["subinterfaces"]["subinterface"]["ipv4"]["addresses"]["address"]["config"].get("ip"))
         table[idx].append(interface["state"]["counters"].get("in-broadcast-pkts"))
         table[idx].append(interface["state"]["counters"].get("in-unicast-pkts"))
         table[idx].append(interface["state"]["counters"].get("in-multicast-pkts"))
         table[idx].append(interface["state"]["counters"].get("out-broadcast-pkts"))
         table[idx].append(interface["state"]["counters"].get("out-unicast-pkts"))
         table[idx].append(interface["state"]["counters"].get("out-multicast-pkts"))

    print(tabulate(table, headers, tablefmt="grid"))





xml_filter = """
     <interfaces xmlns="http://openconfig.net/yang/interfaces">
                <interface>
                    <name>eth1/1</name>
                </interface>
                <interface>
                    <name>eth1/2</name>
                </interface>
                <interface>
                    <name>eth1/3</name>
                </interface>
                <interface>
                    <name>eth1/4</name>
                </interface>
                <interface>
                    <name>eth1/5</name>
                </interface>
                <interface>
                    <name>eth1/6</name>
                </interface>
                <interface>
                    <name>eth1/7</name>
                </interface>
                <interface>
                    <name>eth1/8</name>
               </interface>
            </interfaces>
     """

if node == nodes.core:
    for i in range(0, 4):
        node=nodes.core[i]
        get_request(xml_filter)
else:
    get_request(xml_filter)

