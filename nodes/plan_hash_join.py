    #from plan_cost import get_all_rows_cost

# hash join

# type: inner, outer, anti, left, right, full
from utils import *
from cond_parser import cond_parser
def hash_join (tree):
    operation_name = tree.get_attr("Node Type")
    operation_type = tree.get_attr("Join Type")
    if operation_type != '':
        operation_type += ' '
    #cond_msg = parse_cond(tree.get_attr("Hash Cond").strip('()'))
    cond_msg = cond_parser(tree.get_attr("Hash Cond"))
    rows_result = tree.get_attr("Plan Rows")
    table_name = parse_table_name(tree.get_attr("Hash Cond").strip('()').replace(' ', ''))
    
    msg1 = "{}{} on condition {}".format (operation_type+' ', operation_name, cond_msg)
    if (operation_type == "Anti"):
        msg2 = "The join occurs where not exist {}.".format(cond_msg)
    elif (operation_type == ""):
        msg2 = "The join condition is {}.".format(cond_msg)
    else:
        msg2 = ""
    #msg3 = "The join result consists of {} rows.\n".format(rows_result)
    
    msg = msg1

    
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
