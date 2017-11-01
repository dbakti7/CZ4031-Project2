def index_scan(tree):
    operation_name = tree.get_attr("Node Type")
    table_name = tree.get_attr("Relation Name")
    index_name = tree.get_attr("Index Name")
    direction = tree.get_attr("Scan Direction")

    if direction == "Backward":
        operation_name += " Backward"

    msg = "The DBMS performs {} using {} on {}\n".format(operation_name, index_name, table_name)

    for child in tree.children:
        msg += child.explain()

    return msg
