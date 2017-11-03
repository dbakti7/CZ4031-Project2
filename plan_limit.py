def limit(tree):
    operation_name = tree.get_attr("Node Type")
    plan_rows = tree.get_attr("Plan Rows")
    msg = "The DBMS performs {}, which cuts down the number of rows to the top {} rows.\n".format(operation_name, plan_rows)
    
    for child in tree.children:
        msg += child.explain()

    return msg
