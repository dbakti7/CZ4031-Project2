from index_scan import parseParams

def bitmap(tree):
    paramsMsg = parseParams(tree.params)
    msg = "The DBMS performs {}{} with the condition {}\n".format(tree.node, getMessage(tree), paramsMsg)

    for child in tree.children:
        msg += child.Explain()

    return msg

def getMessage(tree):
    msg = ""

    if 'Heap' in tree.node or 'Index' in tree.node:
        msg = " on {}".format(tree.on)

    return msg
