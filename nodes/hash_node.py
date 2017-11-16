from utils import *

# Node Type: Hash

def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    description = "hashed"
    if (key):
        description += " with condition {}".format(key)
    if(is_branch(planTree)):
        return description + ". "
    parentString = planTree.parent.explain()

    if(parentString == ""):
        return description + ". "

    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString
