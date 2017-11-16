from utils import *

def cte_scan(tree):
    operation_name = tree.get_attr("Node Type")
    table_name = tree.get_attr("Alias")
    msg = "The DBMS performs {} on temporary table {}".format(operation_name, table_name)

    if (is_branch(tree)):
        msg += ". "
        return msg
    
    return msg + tree.parent.explain()
