from utils import *

# Node Type: Function Scan

def function_scan (planNode):
    operation_name = planNode.get_attr("Node Type")
    function_name = planNode.get_attr("Function Name")
    description = "{} on function {}".format (operation_name, function_name)
    
    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString
