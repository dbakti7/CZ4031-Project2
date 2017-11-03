import re
def nested_loop(planTree):
    node = planTree.get_attr("Node Type")
    tablename = planTree.get_attr("Join Filter")
    cond = re.split('=' , tablename)
    description = "The DBMS performs {} on two tables by fetching the result from {} and querying the table {} for each row from the first.".format(
        node, cond[0], con[1])
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
