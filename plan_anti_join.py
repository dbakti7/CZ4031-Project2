from plan_cost import get_all_rows_cost

def anti_join (tree):
    # operationName = getAntiJoinType(tree.node)
    operationName = "Join"
    CondMsg = parse_cond(tree.params)
    cost_all = get_all_rows_cost(tree)
    tableName = parse_table_name(CondMsg)
    #tableName1 = "1"
    #tableName2 = "2"
    # indexName = tree.index #TODO: tree.index is still an assumption on the convention that will be used
    if (CondMsg == ""):
        msg1 = "The DBMS performs {}".format (operationName)
    elif (tableName == ""):
        msg1 = "The DBMS performs {} where not exist the condition {}".format(tree.node, CondMsg)
    else:
        msg1 = "The DBMS performs {} on tables {} where not exist the condition {}".format(tree.node, tableName, CondMsg)
    msg2 = "The cost of performing the {} is {}".format(operationName, cost_all)
    return msg1 + msg2
    
def parse_cond (params):
    if params == []:
        return ""
    else:
        for param in params:
            for word in param.split():
                if word == "Cond:":
                    start = param.index("(") + 1
                    end = param.rindex(")")
                    return param[start:end]

def parse_table_name (CondMsg):
    tableName = []
    for word in CondMsg.split():
        dot = word.find(".")
        if (dot>0):
            name = word[0: (dot)]
            if name not in tableName:
                tableName.append(name)
    end = len(tableName) - 1
    if tableName == []:
        return ""
    elif len(tableName) == 1:
        string = tableName[0]
        return string
    else:
        string = tableName[0]
        for num in range(1,end):
            string += " and " + tableName[num]
        return string

    
        

# 