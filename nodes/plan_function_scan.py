from utils import *

def function_scan (tree):

    operation_name = tree.get_attr("Node Type")
    function_name = tree.get_attr("Function Name")
    msg = "The DBMS performs {} on function {}".format (operation_name, function_name)
    
    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
