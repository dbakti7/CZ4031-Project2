from utils import *

# Node Type: Value Scan

def values_scan(planTree):
    node = planTree.get_attr("Node Type")
    values = planTree.get_attr("Alias")
    description = "{} on {}".format(node, values)

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString
        
    return description + ", " + parentString

