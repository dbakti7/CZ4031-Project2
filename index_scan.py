def index_scan(tree):
    attributes = tree.attributes
    operation_name = attributes["Node Type"]
    table_name = attributes["Relation Name"]
    index_name = attributes["Index Name"]

    msg = "The DBMS performs {} using {} on {}\n".format(operation_name, index_name, table_name)

    for child in tree.children:
        msg += child.explain()

    return msg
