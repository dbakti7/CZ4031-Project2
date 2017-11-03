def function_scan (tree):

    operation_name = tree.get_attr("Node Type")
    function_name = tree.get_attr("Function Name")
    total_cost = tree.get_attr("Total Cost")
    msg = "The DBMS performs {} on function {} at total cost of {}.".format (operation_name, function_name, total_cost)
    
    for child in tree.children:
        msg += child.explain()
    
    return msg