from utils import *

def seq_scan(tree):
    operation_name = "Sequential Scan"
    table_name = tree.get_attr("Relation Name")
    condition = tree.get_attr("Filter")
    condition_msg = ""

    if condition:
        condition_msg += " on condition {}".format(condition)

    msg = "{} on table {}{}".format(operation_name, table_name, condition_msg)
    
    if (is_branch(tree)):
        msg += ". "
        return msg

    parentString = tree.parent.explain()
    if(parentString == ""):
        return msg + ". "
    return msg + ", then it will be " + parentString

