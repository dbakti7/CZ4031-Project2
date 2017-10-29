def seqScan(tree):
    operationName = "Sequential Scan"
    tableName = tree.children[0].children[0].children[0].children[0].children[0].table #TODO: tree.bla3.table is still an assumption on the convention that will be used
    msg = "The DBMS performs {} on table {}".format(operationName, tableName)
    return msg
    
# from plan_parser import PlanParser
# from plan_cost import PlanCost
#
# planParser = PlanParser("plan.txt")
# dummy = planParser.getTree()
#
# # Sequential Scan
# print(seqScan(dummy))
