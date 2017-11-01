def seq_scan(tree):
    attributes = tree.attributes
    operation_name = "Sequential Scan"
    table_name = attributes["Relation Name"]

    condition_msg = ""

    if "Filter" in attributes:
        condition_msg += "on condition {}".format(attributes["Filter"])

    msg = "The DBMS performs {} on table {} {}\n".format(operation_name, table_name, condition_msg)

    for child in tree.children:
        msg += child.explain()

    return msg

