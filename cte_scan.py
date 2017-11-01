def cte_scan(tree):
    operation_name = tree.get_attr("Node Type")
    table_name = tree.get_attr("Alias")
    msg = "The DBMS performs {} on temporary table {}\n".format(operation_name, table_name)

    for child in tree.children:
        msg += child.explain()

    return msg
