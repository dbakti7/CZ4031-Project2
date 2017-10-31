def values_scan(planTree):
    for attr in params:
        valueStr += attr +", " 
    description = "The DBMS performs values scan using values({})".format(
        valueStr[:-2])
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr        
