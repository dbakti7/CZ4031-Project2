from utils import *

# Node Type: Limit

def limit(planNode):
    plan_rows = planNode.get_attr("Plan Rows")
    description = "limited to the top {} rows".format(plan_rows)

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString
        
    return description + ", " + parentString
