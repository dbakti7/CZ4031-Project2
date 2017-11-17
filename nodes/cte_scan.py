# Node Type: Cte Scan

def cte_scan(planNode):
    operation_name = planNode.get_attr("Node Type")
    table_name = planNode.get_attr("Alias")
    description = "The DBMS performs {} on temporary table {}".format(operation_name, table_name)

    if (is_branch(planNode)):
        description += ". "
        return description
        
    return description + planNode.parent.explain()
