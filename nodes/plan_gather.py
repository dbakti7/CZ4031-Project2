from utils import *
def gather(tree):
    #operation_name = tree.get_attr("Node Type")
    #workers_planned = tree.get_attr("Workers Planned")
    msg = ""
    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
        
def gather_merge(tree):
    #operation_name = tree.get_attr("Node Type")
    #workers_planned = tree.get_attr("Workers Planned")
    msg = ""
    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
        
    
