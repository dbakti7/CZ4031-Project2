def indexScan(tree):
    paramsMsg = parseParams(tree.params)
    indexName = tree.using
    tableName = tree.on
    msg = "The DBMS performs {} using index {} on table {} with the condition {}\n".format(tree.node, indexName, tableName, paramsMsg)

    for child in tree.children:
        msg += child.Explain()

    return msg

def parseParams(params):
    paramMsg = "" 

    for item in params:
        if type(item) is not str:
            continue

        if params.index(item) == 0:
            paramMsg += "{}".format(getInfo(item))
        elif params.index(item) == len(params) - 1:
            paramMsg += " AND {}".format(getInfo(item))
        else:
            paramMsg += ", {}".format(getInfo(item))
    return paramMsg

def getInfo(param):
    #TODO: Handler function in main program to handle available params
    start = param.index(":") + 2
    return param[start::]
