def indexScan(tree, **kwargs):
    operationName = getOperationName(kwargs)
    paramsMsg = parseParams(tree.children[1].params)
    indexName = tree.index #TODO: tree.index is still an assumption on the convention that will be used
    tableName = tree.children[0].children[0].children[0].children[0].children[0].table #TODO: tree.bla3.table is still an assumption on the convention that will be used
    msg = "The DBMS performs {} using index {} on table {} with the condition{}".format(operationName, indexName, tableName, paramsMsg)
    return msg

def getOperationName(kwargs):
    operationName = "Index"
    if 'only' in kwargs:
        operationName += " Only"
    if 'backwards' in kwargs:
        operationName += " Backwards"

    operationName += " Scan"
    return operationName
    
def parseParams(params):
    paramMsg = "" 
    for item in params:
        if type(item) is not str:
            continue

        if params.index(item) == 1:
            paramMsg += " {}".format(getInfo(item))
        elif params.index(item) == len(params) - 1:
            paramMsg += " AND {}".format(getInfo(item))
        else:
            paramMsg += ", {}".format(getInfo(item))
    return paramMsg

def getInfo(param):
    #TODO: Handler function in main program to handle available params
    param = str(param)
    start = param.index("(") + 1
    end = param.rindex(")")
    return param[start:end]

# from plan_parser import PlanParser
# from plan_cost import PlanCost
#
# planParser = PlanParser("plan.txt")
# dummy = planParser.getTree()
#
# # Index Scan
# print(indexScan(dummy))
#
# # Index Only Scan
# print(indexScan(dummy, only=True))
#
# # Index Backwards Scan
# print(indexScan(dummy, backwards=True))
#
# # Index Only Backwards Scan
# print(indexScan(dummy, only=True, backwards=True))
