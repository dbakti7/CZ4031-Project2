import re

# Node Type: Nested Loop

def nested_loop(planNode):
    node = planNode.get_attr("Node Type")
    join_type = planNode.get_attr("Join Type")

    if join_type != '':
        join_type += ' '
    join_filter = planNode.get_attr("Join Filter")
    filter_msg = ''
    
    if (join_filter):
        filter_msg = ' on join filter '+join_filter
    description = "{}{}{}".format(
        join_type, node+' Join', filter_msg)
    return description
