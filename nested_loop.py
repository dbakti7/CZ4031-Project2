def nested_loop(planTree):
    description = "The DBMS performs {} on two tables by fetching the result from table {} and querying the table {} for each row from the first.".format(
        planTree.node, table1, table2)
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
