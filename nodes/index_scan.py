from utils import *

def index_scan(tree):
    operation_name = tree.get_attr("Node Type")
    table_name = tree.get_attr("Relation Name")
    index_name = tree.get_attr("Index Name")
    direction = tree.get_attr("Scan Direction")
    filter_condition = tree.get_attr("Index Cond")
    
    if direction == "Backward":
        operation_name += " Backward"
    
    msg = "{} using {} on {}".format(operation_name, index_name, table_name)

    if (filter_condition):
        msg += " with condition {}".format(filter_condition)

    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
