import random
def is_scan_node(planNode):
    node = planNode.get_attr("Node Type")
    if(node in ["Seq Scan", "Index Scan", "Values Scan", "Bitmap Index Scan", "Index Only Scan"]):
        return True
    return False

def get_conjuction():
    return random.choice(["and in the end ", "and ultimately ", "and subsequently ", "and finally ", "and eventually "])

def is_join(planNode):
    if(planNode == None):
        return True
    if(planNode.get_attr("Node Type") in ["Hash Join", "Merge Join", "Nested Loop", "Append"]):
        return True
    return False

def is_branch(planNode):
    if(planNode.parent == None):
        return True
    
    # handling special case of double subplan
    return is_join(planNode.parent) or \
    (planNode.get_attr("Parent Relationship") in ["InitPlan", "SubPlan"] and \
    planNode.parent.get_attr("Parent Relationship") not in ["InitPlan", "SubPlan"])
