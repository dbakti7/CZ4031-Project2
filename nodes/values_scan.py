def values_scan(planTree):
    node = planTree.get_attr("Node Type")
    values = planTree.get_attr("Alias")
    description = "The DBMS performs {} on {}".format(
        node, values)
    childStr = ""
    for child in planTree.children:
        childStr += child.explain() + " "
    return description + " " +childStr        
