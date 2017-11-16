from utils import *

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
        description += " with condition {}".format(key)

    if(is_branch(planTree)):
        return description + ". "

    return description + planTree.parent.explain()
