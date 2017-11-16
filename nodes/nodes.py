from utils import *
def sort(planTree):
    result = ""
    if(is_scan_node(planTree.children[0])):
        result += ", then "
    
    result += "sorted"
    keys = planTree.get_attr("Sort Key")

    if (keys):
        result += " based on "
        size = len(keys)
        for k in keys:
            size -= 1
            result = result + k
            if (size == 1):
                result += k
            elif (size > 1):
                result += ", "

    if (is_branch(planTree)):
        return result + ". "
    
    return result + planTree.parent.explain()

# for Hash Aggregate (hashed) and GroupAggregate (sorted)
# TODO: do we need to specify the technique? seems not that important.
def aggregate(planTree):
    result = ""
    if(is_scan_node(planTree.children[0])):
        result += ", then "
    else:
        result += ", "
    result += "aggregated "
    if(planTree.get_attr("Group Key") != ""):
        result += "based on " + planTree.get_attr("Group Key")[0]
    else:
        result += "to get the " + planTree.get_attr("Output")[0]
    if(is_branch(planTree)):
        return result + ". "
    return result + planTree.parent.explain()

def materialize(planTree):
    result = ""
    for child in planTree.children:
        result = result + child.explain()
    result = result + "The result then is stored (materialized) in the in-memory buffer. "
    return result
