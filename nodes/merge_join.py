from utils import *
from cond_parser import cond_parser
def merge_join(planTree):
    cond = cond_parser(planTree.get_attr("Merge Cond"))
    cond_msg = ""
    if cond != "":
        cond_msg += " on condition {}".format(cond)
    node = planTree.get_attr("Node Type")
    join_type = planTree.get_attr("Join Type")
    description = "{}{}{}".format(
        join_type, node, cond_msg )
    return description
