from utils import *

# Node Type:
#  - Index Scan
#  - Index Only Scan

def index_scan(planNode):
    operation_name = planNode.get_attr("Node Type")
    table_name = planNode.get_attr("Relation Name")
    index_name = planNode.get_attr("Index Name")
    direction = planNode.get_attr("Scan Direction")
    filter_condition = planNode.get_attr("Index Cond")
    if direction == "Backward":
        operation_name += " Backward"
    description = "{} using {} on table {}".format(operation_name, index_name, table_name)
    if (filter_condition):
        description += " with condition {}".format(filter_condition)

    if (is_branch(planNode)):
        description += ". "
        return description

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    return description + ", then it will be " + parentString
