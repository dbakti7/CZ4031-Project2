from utils import *

def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    description = "hashed"


    if (key):
        description += " with condition {}".format(key)

    if(is_branch(planTree)):
        return get_conjuction() + description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return get_conjuction() + description + ". "
    return description + ", " + parentString
