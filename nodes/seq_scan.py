from cond_parser import cond_parser
def seq_scan(tree):
    operation_name = "Sequential Scan"
    table_name = tree.get_attr("Relation Name")
    condition = tree.get_attr("Filter")
    condition_msg = ""
    msg = ""
    # TODO: please check whether seq scan can have children nodes
    for child in tree.children:
        msg += child.explain()

    if condition:
        condition_msg = "on condition {}".format(cond_parser(condition))

    msg += "{} on table {} {}\n".format(operation_name, table_name, condition_msg)

    return msg

