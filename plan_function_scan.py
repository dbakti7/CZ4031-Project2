from plan_cost import getAllRowsCost

def functionScan(tree):
    # assume tableName, columnName
    operationName = "Function Scan"
    # paramsMsg = parseParams(tree.params)
    tableName = tree.tableName
    cost_all = getAllRowsCost(tree)
    # msg = "The DBMS performs {} on table {} with the condition{}".format(operationName, tableName, paramsMsg)
    msg1 = "The DBMS performs {} on table {}. ".format(operationName, tableName)
    msg2 = "The cost of performing the {} is {}".format(operationName, cost_all)
    return msg1 + msg2
    
    
    
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
