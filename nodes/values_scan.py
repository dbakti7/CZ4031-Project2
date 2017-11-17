from utils import *

# Node Type: Value Scan

def values_scan(planNode):
    node = planNode.get_attr("Node Type")
    values = planNode.get_attr("Alias")
    description = "{} on {}".format(node, values)

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString
        
    return description + ", " + parentString

