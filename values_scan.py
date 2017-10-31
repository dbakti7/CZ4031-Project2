def valuesScan(planTree):
    params = planTree.param[0]
    for attr in params:
        valueStr += attr +", " 
    description = "The DBMS performs values scan using values({})".format(
        valueStr[:-2])
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr        
