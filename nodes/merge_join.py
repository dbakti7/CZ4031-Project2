from utils import *

# Node Type: Merge Join

def merge_join(planNode):
    cond = planNode.get_attr("Merge Cond")
    cond_msg = ""
    if (cond):
        cond_msg += " on condition {}".format(cond)
    node = planNode.get_attr("Node Type")
    join_type = planNode.get_attr("Join Type")
    if join_type != "":
        join_type += ' '
    description = "{}{}{}".format(
        join_type, node, cond_msg )
    return description
