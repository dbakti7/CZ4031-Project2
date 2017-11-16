import re
def nested_loop(planTree):
    node = planTree.get_attr("Node Type")
    join_type = planTree.get_attr("Join Type")
    if join_type != '':
        join_type += ' '
    join_filter = planTree.get_attr("Join Filter")
    filter_msg = ''
    if (join_filter):
        filter_msg = ' on join filter '+join_filter
    description = "{}{}{}".format(
        join_type, node+' Join', filter_msg)
    return description
