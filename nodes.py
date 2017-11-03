def sort(planTree):
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
