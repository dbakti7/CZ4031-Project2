# Node Type: Hash Join

def hash_join (tree):
    operation_name = tree.get_attr("Node Type")
    operation_type = tree.get_attr("Join Type")
    cond_msg = tree.get_attr("Hash Cond")
    if operation_type != '':
        operation_type += ' '
    if (cond_msg):
        cond_msg = ' on condition '+cond_msg
    msg = "{}{}{}".format (operation_type, operation_name, cond_msg)
    return msg
