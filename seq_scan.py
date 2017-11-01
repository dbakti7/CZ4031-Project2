def seq_scan(tree):
    operation_name = "Sequential Scan"
    table_name = tree.get_attr("Relation Name")
    condition = tree.get_attr("Filter")
    condition_msg = ""

    if condition:
        condition_msg += "on condition {}".format(condition)

    msg = "The DBMS performs {} on table {} {}\n".format(operation_name, table_name, condition_msg)

    for child in tree.children:
        msg += child.explain()

    return msg

