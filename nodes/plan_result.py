# Node Type: Result

def result(planNode):
    plan_rows = planNode.get_attr("Plan Rows")
    description = "{} row(s) are obtained as the result".format(plan_rows)

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString