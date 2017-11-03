def limit(tree):
    operation_name = tree.get_attr("Node Type")
    plan_rows = tree.get_attr("Plan Rows")
    actual_rows = tree.get_attr("Actual Rows")
    msg = "The DBMS performs {}, which cuts down the number of rows to the top {} rows. As a result, the table now have only {} rows.".format(operation_name, plan_rows, actual_rows)
    
    for child in tree.children:
        msg += child.explain()

    return msg
