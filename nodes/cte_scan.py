# Node Type: Cte Scan

def cte_scan(planNode):
    operation_name = planNode.get_attr("Node Type")
    table_name = planNode.get_attr("Alias")
    description = "{} on temporary table {}".format(operation_name, table_name)

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString
