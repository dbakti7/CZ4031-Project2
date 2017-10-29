# cost1 = time taken for 1st row
# cost2 = time taken for all rows

def getOneRowsCost(tree):
    one_cost = "{} - Cost of execution of first row :{}".format(tree.data, tree.cost1)
    return one_cost
    
def getAllRowsCost(tree):
    all_cost = "{} - Cost of execution of all rows :{}".format(tree.data, tree.cost2)
    return all_cost
    
def getRowNum(tree):
    rows = "{} - Number of rows executed :{}".format(tree.data, tree.rows)
    return rows
    
def getRowWidth(tree):
    width = "{} - Width of each row :{}".format(tree.data, tree.width)
    return width
    
    
        #print(one_cost)
        #print(all_cost)
        #print(rows)
        #print(width)

    
    
