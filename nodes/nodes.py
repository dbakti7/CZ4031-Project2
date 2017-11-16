from utils import *

# Node Type: Sort

def sort(planTree):
    description = "sorted"
    keys = planTree.get_attr("Sort Key")
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

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

# Node Type:
#   - Hash Aggregate (hashed)
#   - GroupAggregate (sorted)

def aggregate(planTree):
    description = "aggregated "
    if(planTree.get_attr("Group Key") != ""):
        description += "based on table " + planTree.get_attr("Group Key")[0]
    else:
        description += "to get the " + planTree.get_attr("Output")[0]

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

# Node Type: Materialize

def materialize(planTree):
    description = "materialized"

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

