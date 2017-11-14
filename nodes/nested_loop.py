import re
def nested_loop(planTree):
    node = planTree.get_attr("Node Type")
    tablename = planTree.get_attr("Join Filter")
    table_exist = ''
    if tablename != '':
        table_exist = ' using join filter '+tablename
    description = "The DBMS performs {}{}.".format(
        node, table_exist)
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
