# cost1 = time taken for 1st row
# cost2 = time taken for all rows

def get_one_rows_cost(tree):
    one_cost = "Time taken for the execution initial start-up is {}".format(tree.get_attr("Actual Startup Time"))
    return one_cost
    
def get_all_rows_cost(tree):
    all_cost = " Estimated query time is {}.".format(tree.get_attr("Actual Total Time"))
    return all_cost
    
def get_row_num(tree):
    rows = "Number of rows executed is {}".format(tree.get_attr("Actual Rows"))
    return rows
    
