def get_execution_cost(planNode):
    all_cost = "The estimated query result is {}, with estimated query cost of {}.".format(planNode.get_attr("Plan Rows"), planNode.get_attr("Total Cost"))
    return all_cost