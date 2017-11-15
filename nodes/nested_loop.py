import re
def nested_loop(planTree):
    childStr = ""
    for i in range(len(planTree.children)):
        child = planTree.children[i]
        childStr += child.explain()
        if(i == 0):
            childStr += " This will be joined with "
    return childStr
    node = planTree.get_attr("Node Type")
    tablename = planTree.get_attr("Join Filter")
    table_exist = ''
    if tablename != '':
        table_exist = ' using join filter '+tablename
    description = "The DBMS performs {}{}.".format(
        node, table_exist)
    childStr = ""
    
    return description + childStr
