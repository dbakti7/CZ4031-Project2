def functionScan(tree):
    # assume tableName, columnName
    operationName = "Function Scan"
    # paramsMsg = parseParams(tree.params)
    tableName = tree.tableName
    # msg = "The DBMS performs {} on table {} with the condition{}".format(operationName, tableName, paramsMsg)
    msg = "The DBMS performs {} on table {}".format(operationName, tableName)
    return msg
    
    
    
#def parseParams(params):
#    paramMsg = "" 
#    for item in params:
#        paramMsg+= " {}".format(getInfo(item))
#    return paramMsg
#
#def getInfo(param):
#    start = param.index("(") + 1
#    end = param.rindex(")")
#    return param[start:end]

# dummy = {"tableName": "tablename", "indexName": "indexname", "params": ["Index Cond: (c1 > 500)"]}
# print(functionScan(dummy))
