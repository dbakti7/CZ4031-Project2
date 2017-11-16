from utils import *
from cond_parser import cond_parser

def index_scan(tree):
    operation_name = tree.get_attr("Node Type")
    table_name = tree.get_attr("Relation Name")
    index_name = tree.get_attr("Index Name")
    direction = tree.get_attr("Scan Direction")
    filter_condition = tree.get_attr("Index Cond")
    
    if direction == "Backward":
        operation_name += " Backward"
    
    msg = "{} using {} on {}\n".format(operation_name, index_name, table_name)

    if (filter_condition):
        msg += " with condition {}".format(cond_parser(filter_condition))

    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
