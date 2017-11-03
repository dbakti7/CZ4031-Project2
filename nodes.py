def sort(planTree):
    result = "The sort is performed with " + planTree.attributes["Sort Method"] + ". "
    for child in planTree.children:
        result = result + child.explain()
    return result

# for Hash Aggregate (hashed) and GroupAggregate (sorted)
# TODO: do we need to specify the technique? seems not that important.
def aggregate(planTree):
    result = "The results are grouped by " 
    size = len(planTree.attributes["Group Key"])
    #TODO: get the column name and table name from the format
    # table_name.column_name (can it be alias instead?)
    for i in range(size):
        result = result + planTree.attributes["Group Key"][i]
        if(size > 1):
            if(i == size - 2):
                result = result + " and "
            elif(i != size - 1):
                result = result + ", "
    result = result + ". "
    for child in planTree.children:
        result = result + child.explain()
    return result
