def append(tree):
    msg = "Perform multiple sub-operations:\n"
    
    count = 0
    for item in tree.children:
        count += 1
        msg += "{}. {}".format(count, item.explain())

    return msg
