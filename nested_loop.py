def nestedLoop(planTree):
    description = "Joins two tables by fetching the result from table {} and querying the table {} for each row from the first.".format(
        table1, table2)
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
