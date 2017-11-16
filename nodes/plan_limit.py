from utils import *
def limit(planTree):
    plan_rows = planTree.get_attr("Plan Rows")
    description = "limited to {} rows".format(plan_rows)

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "
    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString
    return description + ", " + parentString
