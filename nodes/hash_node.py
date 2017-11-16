from utils import *
from cond_parser import cond_parser

def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    description = ""

    if(is_scan_node(planTree.children[0])):
        description += ", then "
    else:
        description += ", "
    description += "hashed"

    if (key):
        description += " with condition {}".format(cond_parser(key))

    if(is_branch(planTree)):
        return description + ". "

    return description + planTree.parent.explain()
