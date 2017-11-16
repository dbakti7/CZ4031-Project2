from utils import *
def sort(planTree):
    result = "sorted"
    keys = planTree.get_attr("Sort Key")

    if (keys):
        result += " based on "
        size = len(keys)
        for k in keys:
            size -= 1
            result = result + k
            if (size == 1):
                result += ", and "
            elif(size > 1):
                result += ", "

    if (is_branch(planTree)):
        return get_conjuction() + result + ". "
    parentString = planTree.parent.explain()
    if(parentString == ""):
        return get_conjuction() + result + ". "
    return result + ", " + parentString

# for Hash Aggregate (hashed) and GroupAggregate (sorted)
# TODO: do we need to specify the technique? seems not that important.
def aggregate(planTree):
    
    result = "aggregated "
    if(planTree.get_attr("Group Key") != ""):
        result += "based on " + planTree.get_attr("Group Key")[0]
    else:
        result += "to get the " + planTree.get_attr("Output")[0]
    if(is_branch(planTree)):
        return get_conjuction() + result + ". "
    parentString = planTree.parent.explain()
    if(parentString == ""):
        return get_conjuction() + result + ". "
    return result + ", " + parentString

def materialize(planTree):
    result = ""

    if (is_branch(planTree)):
        result += " and then materialized"
        return result + ". "
    else:
        result += ", materialized"

    return result + planTree.parent.explain()
   
