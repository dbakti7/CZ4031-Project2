from utils import *

# Node Type: Seq Scan

def seq_scan(planNode):
    operation_name = "Sequential Scan"
    table_name = planNode.get_attr("Relation Name")
    condition = planNode.get_attr("Filter")
    condition_msg = ""
    if condition:
        condition_msg += " on condition {}".format(condition)
    description = "{} on table {}{}".format(operation_name, table_name, condition_msg)

    if (is_branch(planNode)):
        description += ". "
        return description

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "
        
    return description + ", then it will be " + parentString

