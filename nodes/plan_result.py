# Node Type: Result

def result(tree):
    plan_rows = tree.get_attr("Plan Rows")
    msg = "The DBMS obtains {} rows as a result".format(plan_rows)
    for child in tree.children:
        msg += child.explain()
    return msg
    