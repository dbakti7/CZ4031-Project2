from utils import *

# Node Type: Function Scan

def function_scan (planNode):
    operation_name = planNode.get_attr("Node Type")
    function_name = planNode.get_attr("Function Name")
    description = "The DBMS performs {} on function {}".format (operation_name, function_name)
    
    if (is_branch(planNode)):
        description += ". "
        return description

    return description + planNode.parent.explain()
