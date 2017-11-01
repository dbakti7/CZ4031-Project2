def bitmap(tree):
    attributes = tree.attributes
    operation_name = attributes["Node Type"]

    msg = "The DBMS performs {} {}\n".format(operation_name, get_message(attributes))

    for child in tree.children:
        msg += child.explain()

    return msg

def get_message(attributes):
    msg = ""
    node = attributes["Node Type"]

    if "Heap" in node:
        msg += "on table {} with recheck condition {}".format(attributes["Relation Name"], attributes["Recheck Cond"])
    elif "Index" in node:
        msg += "on index {} with index condition {}".format(attributes["Index Name"], attributes["Index Cond"])

    return msg
