def unique(tree):
    msg = "Remove duplicate values\n"

    for child in tree.children:
        msg += child.explain()

    return msg

