def result(tree):
    #operation_name = tree.get_attr("Node Type")
    msg = ""
    for child in tree.children:
        msg += child.explain()

    plan_rows = tree.get_attr("Plan Rows")
    msg += "The DBMS obtains {} rows as a result".format(plan_rows)
    
    
        
    return msg
    