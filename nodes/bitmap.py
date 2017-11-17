from utils import *

# Node Type: 
#  - Bitmap Heap Scan
#  - Bitmap Index Scan
#  - BitmapAnd
#  - BitmapOr

def bitmap(planNode):
    operation_name = planNode.get_attr("Node Type")
    description = "{} {}".format(operation_name, get_message(planNode))
    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def get_message(planNode):
    description = ""
    node = planNode.get_attr("Node Type")
    if "Heap" in node:
        description += "on table {} with recheck condition {}".format(planNode.get_attr("Relation Name"), planNode.get_attr("Recheck Cond"))
    elif "Index" in node:
        description += "on index {} with index condition {}".format(planNode.get_attr("Index Name"), planNode.get_attr("Index Cond"))
    return description
