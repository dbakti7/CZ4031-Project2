def gather(tree):
    operation_name = tree.get_attr("Node Type")
    workers_planned = tree.get_attr("Workers Planned")
    msg = "The DBMS performed {} on the {} parallel processing done in the query.\n".format(operation_name, workers_planned)
    
    
    for child in tree.children:
        msg += child.explain()
        
    return msg
    