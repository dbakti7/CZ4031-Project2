import re
def nested_loop(planTree):
    node = planTree.get_attr("Node Type")
    join_type = planTree.get_attr("Join Type")
    join_filter = planTree.get_attr("Join Filter")
    if join_filter != '':
        join_filter = ' with join filter '+ join_filter
    description = "The DBMS performs {} {} join{}. ".format(
        node, join_type, join_filter)   
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
