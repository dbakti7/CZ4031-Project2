from utils import *

def seq_scan(planNode):
    """
        Handler function for sequential scan.
        Node Type:  Seq Scan
    """
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

def index_scan(planNode):
    """
        Handler function for index scan.
        Node Type: Index Scan, Index Only Scan
    """
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

def bitmap(planNode):
    """
        Handler function for bitmap scan.
        Node Type: Bitmap Heap Scan, Bitmap Index Scan, BitmapAnd, BitmapOr
    """
    operation_name = planNode.get_attr("Node Type")
    description = "{} {}".format(operation_name, get_bitmap_message(planNode))
    
    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def values_scan(planNode):
    """
        Handler function for value scan.
        Node Type: Value Scan
    """
    node = planNode.get_attr("Node Type")
    values = planNode.get_attr("Alias")
    description = "{} on {}".format(node, values)

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString
        
    return description + ", " + parentString

def get_bitmap_message(planNode):
    """
        Utility function to get message for bitmap scan
    """
    description = ""
    node = planNode.get_attr("Node Type")
    if "Heap" in node:
        description += "on table {} with recheck condition {}".format(planNode.get_attr("Relation Name"), planNode.get_attr("Recheck Cond"))
    elif "Index" in node:
        description += "on index {} with index condition {}".format(planNode.get_attr("Index Name"), planNode.get_attr("Index Cond"))
    return description
