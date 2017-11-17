# Node Type: Hash Join

def hash_join (planNode):
    operation_name = planNode.get_attr("Node Type")
    operation_type = planNode.get_attr("Join Type")
    cond_msg = planNode.get_attr("Hash Cond")
    if operation_type != '':
        operation_type += ' '
    if (cond_msg):
        cond_msg = ' on condition '+cond_msg
    description = "{}{}{}".format (operation_type, operation_name, cond_msg)
    return description
