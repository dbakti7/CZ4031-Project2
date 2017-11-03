#from plan_cost import get_all_rows_cost

# hash join

# type: inner, outer, anti, left, right, full

def hash_join (tree):

    operation_name = tree.get_attr("Node Type")
    operation_type = tree.get_attr("Join Type")
    cond_msg = parse_cond(tree.get_attr("Hash Cond"))
    rows_result = tree.get_attr("Actual Rows")
    table_name = parse_table_name(cond_msg)
    
    msg1 = "The DBMS performs {} {} on table {}.".format (operation_type, operation_name, table_name)
    if (operation_type == "Anti"):
        msg2 = "The join occurs where not exist {}".format(cond_msg)
    elif (operation_type == ""):
        msg2 = "The join condition is {}".format(cond_msg)
    else:
        msg2 = ""
    msg3 = "The join result consist of {} rows".format(rows_result)
    
    msg = msg1 + msg2 + msg3
    
    for child in tree.children:
        msg += child.explain()

    
    return msg
    
def parse_cond (cond):
    if cond == []:
        return ""
    else:
        return cond.replace(" = ", " is equal to ")

def parse_table_name (cond_msg):
    tableName = []
    for word in cond_msg.split():
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