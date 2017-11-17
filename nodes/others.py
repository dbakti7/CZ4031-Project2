from utils import *

def hash_node(planNode):
    """
        Handler function for hash.
        Node Type: Hash
    """
    node = planNode.get_attr("Node Type")
    key = planNode.get_attr("Hash Cond")
    description = "hashed"
    if (key):
        description += " with condition {}".format(key)

    if(is_branch(planNode)):
        return description + ". "
    parentString = planNode.parent.explain()

    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def sort(planNode):
    """
        Handler function for sort.
        Node Type: Sort
    """
    description = "sorted"
    keys = planNode.get_attr("Sort Key")
    if (keys):
        description += " based on "
        size = len(keys)
        for k in keys:
            size -= 1
            description = description + k
            if (size == 1):
                description += ", and "
            elif(size > 1):
                description += ", "

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def aggregate(planNode):
    """
        Handler function for aggregate.
        Node Type: Aggregate
    """
    description = "aggregated "
    if(planNode.get_attr("Group Key") != ""):
        description += "based on table " + planNode.get_attr("Group Key")[0]
    else:
        description += "to get the " + planNode.get_attr("Output")[0]

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def materialize(planNode):
    """
        Handler function for materialize.
        Node Type: Materialize
    """
    description = "materialized"

    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def unique(planNode):
    """
        Handler function for unique.
        Node Type: Unique
    """
    description = "eliminate the duplicate values"
    
    if(is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "

    if(planNode.parent != None and is_branch(planNode.parent)):
        return description + ", " + get_conjuction() + parentString

    return description + ", " + parentString

def limit(planNode):
    """
        Handler function for limit.
        Node Type: Limit
    """
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

def result(planNode):
    """
        Handler function for result.
        Node Type: Result
    """
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

def gather(planNode):
    """
        Handler function for gather.
        Node Type: Gather, Gather Merge
    """
    description = ""
    if (is_branch(planNode)):
        description += ". "
        return description
    return description + planNode.parent.explain()

def cte_scan(planNode):
    """
        Handler function for CTE scan.
        Node Type: Cte Scan
    """
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

def function_scan (planNode):
    """
        Handler function for function scan.
        Node Type: Function Scan
    """
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

def subquery_scan(planNode):
    """
        Handler function for subquery scan.
        Node Type: Subquery Scan
    """
    node = planNode.get_attr("Node Type")
    subquery_name = planNode.get_attr("Alias")
    filterValue = planNode.get_attr("Filter")
    description = ''
    if filterValue != '':
        description = "scan is performed with filter " + filterValue + " "
        if(subquery_name != ''):
            description += "and "
    if subquery_name != '':
        description += "this subquery is called {}".format(subquery_name)

    if (is_branch(planNode)):
        return description + ". "

    parentString = planNode.parent.explain()
    if(parentString == ""):
        return description + ". "
    return description + ", " + parentString


