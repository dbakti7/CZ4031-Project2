def seq_scan(tree):
    operation_name = "Sequential Scan"
    table_name = tree.get_attr("Relation Name")
    condition = tree.get_attr("Filter")
    condition_msg = ""

    if condition:
        condition_msg += "on condition {}".format(condition)

    msg = "{} on table {} {}".format(operation_name, table_name, condition_msg)
    
    if(len(tree.parent.children) > 1):
        return msg
    return msg + tree.parent.explain()    

