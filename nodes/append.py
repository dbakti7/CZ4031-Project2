def append(tree):
    msg = "Perform multiple sub-operations:\n"
    
    count = 0
    for child in tree.children:
        count += 1
        msg += "{}. {}".format(count, child.explain())

    return msg
