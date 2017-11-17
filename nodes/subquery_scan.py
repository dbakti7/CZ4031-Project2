from utils import *

# Node Type: Subquery Scan

def subquery_scan(planNode):
    node = planNode.get_attr("Node Type")
    subquery_name = planNode.get_attr("Alias")
    description = ''
    if subquery_name != '':
        description = "this subquery is called {}".format(subquery_name)

    if (is_branch(planNode)):
        return get_conjuction() + description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return get_conjuction() + description + ". "
    return description + ", " + parentString
