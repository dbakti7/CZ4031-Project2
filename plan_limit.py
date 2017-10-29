from plan_cost import getAllRowsCost

def limit(tree):
    operationName = "Limit"
    limitRows = tree.rows
    tableName = tree.children[0].on
    cost_all = getAllRowsCost(tree)
    msg = "The DBMS performs {} to {} rows on table {}".format(operationName, limitRows, tableName)
    msg2 = "The cost of performing the {} is {}".format(operationName, cost_all)
    return msg + msg2
    
# dummy = {"tableName": "tablename", "rows": "10"}
# print(limit(dummy))
