def cte_scan(tree):
    attributes = tree.attributes
    operation_name = attributes["Node Type"]
    table_name = attributes["Relation Name"]
    msg = "The DBMS performs {} on table {}\n".format(operation_name, table_name)

    for child in tree.children:
        msg += child.explain()

    return msg
