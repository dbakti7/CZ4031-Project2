def subquery_scan(planTree):
    node = planTree.get_attr("Node Type")
    subqueryname = planTree.get_attr("Alias")
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()

    childStr += ". "

    #description = "The DBMS performs {} on subquery {}. ".format(
    #   node, subqueryname)
    description = "This subquery is scanned"
    
    return childStr + description
