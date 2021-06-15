import sys
import nodes
from tabulate import tabulate



def check_input_node(sys):
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
    
    return node;