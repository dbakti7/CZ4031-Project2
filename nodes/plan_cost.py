def get_execution_cost(planNode):
    all_cost = " Estimated query time is {}.".format(planNode.get_attr("Actual Total Time"))
    return all_cost