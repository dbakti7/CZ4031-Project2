from utils import *
def sort(planTree):
    result = ""
    if(is_scan_node(planTree.children[0])):
        result += ", then "
    
    result += "sorted"
    if(is_branch(planTree)):
        return result + ". "
    
    return result + planTree.parent.explain()
    result = ""
    keys = planTree.get_attr("Sort Key")
    if(keys):
        result = "The results are sorted based on "
        size = len(keys)
        for k in keys:
            size -= 1
            result = result + k
            if(size == 1):
                result = result + " and "
            elif (size > 1):
                result = result + ", "

    if(planTree.get_attr("Sort Method")):
        result = result + " with " + planTree.get_attr("Sort Method") + " method. "
    else:
        result = result + ". "
    
    for child in planTree.children:
        result = result + child.explain()
    return result

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
    result = ""
    keys = planTree.get_attr("Group Key")
    if(keys):
        result = "The results are grouped by " 
        size = len(keys)
        # TODO: get the column name and table name from the format
        # table_name.column_name (can it be alias instead?)
        for i in range(size):
            result = result + keys[i]
            if(size > 1):
                if(i == size - 2):
                    result = result + " and "
                elif(i != size - 1):
                    result = result + ", "
        result = result + ". "
    for child in planTree.children:
        result = result + child.explain()
    return result

def materialize(planTree):
    result = ""
    for child in planTree.children:
        result = result + child.explain()
    result = result + "The result then is stored (materialized) in the in-memory buffer. "
    return result