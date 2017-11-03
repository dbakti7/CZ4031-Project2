def subquery_scan(planTree):
    node = planTree.get_attr("Node Type")
    subqueryname = planTree.get_attr("Alias")
    description = "The DBMS performs {} on subquery {}. ".format(
        node, subqueryname)
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
