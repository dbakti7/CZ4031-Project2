#from plan_cost import get_all_rows_cost

# hash join

# type: inner, outer, anti, left, right, full
from cond_parser import cond_parser
def hash_join (tree):
    msg = ""
    for i in range (len(tree.children)):
        child = tree.children[i]
        if(tree.isRightLeaf):
            if(i == 0):
                msg += "We perform "
            else:
                msg += "After that, we perform "
        msg += child.explain()
        if(not tree.isRightLeaf):
            if(i == 0):
                msg += "This will be joined with "
                if(tree.rightLeaf[0] == "Join"):
                    msg += "the result of join operation between " + tree.rightLeaf[1][0] + " and " + tree.rightLeaf[1][1] + ". "
                else:
                    msg += str(tree.rightLeaf[1]) + ". "
            else:
                msg += "This join result will be the right hand side to be joined with " + tree.leftLeaf[1] + " table on condition " + cond_parser(tree.get_attr("Hash Cond")) + ". " + tree.get_attr("Hash Cond") + ". "
    return msg

    operation_name = tree.get_attr("Node Type")
    operation_type = tree.get_attr("Join Type")
    cond_msg = parse_cond(tree.get_attr("Hash Cond").strip('()'))
    rows_result = tree.get_attr("Plan Rows")
    table_name = parse_table_name(tree.get_attr("Hash Cond").strip('()').replace(' ', ''))
    
    msg1 = "The DBMS performs {} {} on table {}.\n".format (operation_type, operation_name, table_name)
    if (operation_type == "Anti"):
        msg2 = "The join occurs where not exist {}.\n".format(cond_msg)
    elif (operation_type == ""):
        msg2 = "The join condition is {}.\n".format(cond_msg)
    else:
        msg2 = ""
    msg3 = "The join result consists of {} rows.\n".format(rows_result)
    
    msg = msg1 + msg2 + msg3
    
    

    
    return msg
    
def parse_cond (cond):
    if cond == []:
        return ""
    else:
        return cond.replace(" = ", " is equal to ")

def parse_table_name (cond_msg):
    tableName = []
    #table_name = ""
    cond_list = cond_msg.split("=")
    for word in cond_list:
        dot = word.find('.')
        word_new = word[0:int(dot)]
        tableName.append(word_new)
    return ' and '.join(tableName)
#    if len(tableName) == 0:
#        return table_name
#    elif len(tableName) == 1:
#        table_name = tableName[0]
#        return table_name
#    else:
#        table_name = tableName[0]
#        for num in range(1,len(tableName) - 1):
#            table_name += " and " + tableName[num]
#        return table_name

    
        

# 