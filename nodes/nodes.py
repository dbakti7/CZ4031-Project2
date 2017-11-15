from utils import is_scan_node
from utils import is_join
from utils import get_conjuction

def sort(planTree):
    result = ""
    for i in range(len(planTree.children)):
        child = planTree.children[i]
        result = result + child.explain()
        if(is_scan_node(child)):
            result += ", then "
        elif(is_join(child)):
            result += "The join result is then "
        elif(is_join(planTree.parent) and not (is_join(planTree.children[0]) or (len(planTree.children) > 1 and is_join(planTree.children[1])))):
            result += get_conjuction()
    keys = planTree.get_attr("Sort Key")
    if(keys):
        #result = "The results are sorted based on "
        result += "sorted based on "
        size = len(keys)
        for k in keys:
            size -= 1
            result = result + k
            if(size == 1):
                result = result + " and "
            elif (size > 1):
                result = result + ", "
    if(is_join(planTree.parent)):
        result += ". "
    return result

    if(planTree.get_attr("Sort Method")):
        result = result + " with " + planTree.get_attr("Sort Method") + " method. "
    else:
        result = result + ". "
    
    
    return result

# for Hash Aggregate (hashed) and GroupAggregate (sorted)
# TODO: do we need to specify the technique? seems not that important.
def aggregate(planTree):
    result = ""
    keys = planTree.get_attr("Group Key")
    for i in range(len(planTree.children)):
        child = planTree.children[i]
        result = result + child.explain()
        if(i == len(planTree.children) - 1):
            result += ", "
            if(is_scan_node(child)):
                result += "then "
            elif(is_join(planTree.parent) and not (is_join(planTree.children[0]) or (len(planTree.children) > 1 and is_join(planTree.children[1])))):
                result += get_conjuction()
    if(keys):
        #result = "The results are grouped by " 
        result += "grouped by "
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
        #result = result + ". "
    else:
        result += "we get the min value of " + planTree.get_attr("Output")[0] + ". "
    if(is_join(planTree.parent)):
        result += ". "
    return result

def materialize(planTree):
    result = ""
    for i in range(len(planTree.children)):
        child = planTree.children[i]
        result = result + child.explain()
        result += ", "
        if(is_scan_node(child)):
            result += "then "
        elif(is_join(planTree.parent) and not (is_join(planTree.children[0]) or (len(planTree.children) > 1 and is_join(planTree.children[1])))):
            result += get_conjuction()
    result = result + "is stored (materialized) in the in-memory buffer"
    if(is_join(planTree.parent)):
        result += ". "
    return result