from utils import *

# Node Type: Hash

def hash_node(planNode):
    node = planNode.get_attr("Node Type")
    key = planNode.get_attr("Hash Cond")
    description = "hashed"
    if (key):
        description += " with condition {}".format(key)

    if(is_branch(planNode)):
        return description + ". "
    parentString = planNode.parent.explain()

    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString
