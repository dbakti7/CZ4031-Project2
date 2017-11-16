import re
from cond_parser import cond_parser
def nested_loop(planTree):
    node = planTree.get_attr("Node Type")
    join_type = planTree.get_attr("Join Type")
    join_filter = cond_parser(planTree.get_attr("Join Filter"))
    filter_msg = ''
    if join_filter != '':
        filter_msg = ' on join filter '+join_filter
    description = "{}{}{}".format(
        join_type, node, filter_msg)
    return description
