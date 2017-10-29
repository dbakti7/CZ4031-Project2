from index_scan import parseParams

def bitmap(tree, *args):
    operationName = getOperationName(args[0])
    paramsMsg = parseParams(tree.children[1].params)
    indexName = "index"
    tableName = tree.children[0].children[0].children[0].children[0].children[0].table #TODO: tree.bla3.table is still an assumption on the convention that will be used
    msg = "The DBMS performs {}{} with the condition{}".format(operationName, getMessage(args[0], tableName, indexName), paramsMsg)
    return msg

def getOperationName(arg):
    operationName = "Bitmap"

    if arg == 'heap':
        operationName += " Heap Scan"
    elif arg == 'index':
        operationName += " Index Scan"
    else:
        operationName += arg

    return operationName

def getMessage(arg, tableName, indexName):
    msg = ""

    if arg == 'heap':
        msg = " on {}".format(tableName)
    elif arg == 'index':
        msg = " on {}".format(indexName)

    return msg

# from plan_parser import PlanParser
# from plan_cost import PlanCost
#
# planParser = PlanParser("plan.txt")
# dummy = planParser.getTree()
#
# # Bitmap Heap Scan
# print(bitmap(dummy, "heap"))
#
# # Bitmap Index Scan
# print(bitmap(dummy, "index"))
#
# # BitmapOr
# print(bitmap(dummy, "OR"))
#
# # BitmapAnd
# print(bitmap(dummy, "AND"))
