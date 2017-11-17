def hash_join (planNode):
    """
        Handler function for hash join.
        Node Type: Hash Join
    """
    operation_name = planNode.get_attr("Node Type")
    operation_type = planNode.get_attr("Join Type")
    cond_msg = planNode.get_attr("Hash Cond")

    if operation_type != '':
        operation_type += ' '
        
    if (cond_msg):
        cond_msg = ' on condition '+cond_msg
    description = "{}{}{}".format (operation_type, operation_name, cond_msg)
    return description

def nested_loop(planNode):
    """
        Handler function for nested loop join.
        Node Type: Nested Loop
    """
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

def merge_join(planNode):
    """
        Handler function for merge join.
        Node Type: Merge Join
    """
    cond = planNode.get_attr("Merge Cond")
    cond_msg = ""
    
    if (cond):
        cond_msg += " on condition {}".format(cond)
    node = planNode.get_attr("Node Type")
    join_type = planNode.get_attr("Join Type")

    if join_type != "":
        join_type += ' '
    description = "{}{}{}".format( join_type, node, cond_msg )
    return description

def append(planNode):
    """
        Handler function for append.
        Node Type: Append
    """
    description = "append operation"
    return description


