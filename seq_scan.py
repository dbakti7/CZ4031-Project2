from index_scan import parseParams

def seqScan(tree):
    operationName = "Sequential Scan"
    tableName = tree.on
    paramsMsg = parseParams(tree.params)
    msg = "The DBMS performs {} on table {} on condition {}\n".format(operationName, tableName, paramsMsg)

    for child in tree.children:
        msg += child.Explain()

    return msg

