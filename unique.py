def unique(tree):
    msg = "Remove duplicate values\n"

    for item in tree.children:
        msg += item.explain()

    return msg

