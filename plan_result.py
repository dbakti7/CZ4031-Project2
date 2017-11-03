def result(tree):
    #operation_name = tree.get_attr("Node Type")
    plan_rows = tree.get_attr("Plan Rows")
    msg = "The DBMS obtains {} rows as a result the query.\n".format(plan_rows)
    
    for child in tree.children:
        msg += child.explain()
        
    return msg
    