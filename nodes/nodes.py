from utils import *

# Node Type: Sort

def sort(planNode):
    description = "sorted"
    keys = planNode.get_attr("Sort Key")
    if (keys):
        description += " based on "
        size = len(keys)
        for k in keys:
            size -= 1
            description = description + k
            if (size == 1):
                description += ", and "
            elif(size > 1):
                description += ", "

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

# Node Type:
#   - Hash Aggregate (hashed)
#   - GroupAggregate (sorted)

def aggregate(planNode):
    description = "aggregated "
    if(planNode.get_attr("Group Key") != ""):
        description += "based on table " + planNode.get_attr("Group Key")[0]
    else:
        description += "to get the " + planNode.get_attr("Output")[0]

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

# Node Type: Materialize

def materialize(planNode):
    description = "materialized"

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

