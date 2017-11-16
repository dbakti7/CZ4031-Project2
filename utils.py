import random
def is_scan_node(planTree):
    node = planTree.get_attr("Node Type")
    #TODO: do we need to include Subquery Scan?
    if(node in ["Seq Scan", "Index Scan", "Bitmap Heap Scan", "Values Scan", "Bitmap Index Scan", "Index Only Scan"]):
        return True
    return False

def get_conjuction():
    return random.choice(["and ", "and finally ", "and eventually "])

def is_join(planTree):
    if(planTree == None):
        return True
    if(planTree.get_attr("Node Type") in ["Hash Join", "Merge Join", "Nested Loop"]):
        return True
    return False

def is_branch(planTree):
    if(planTree.parent == None):
        return True
    #return len(planTree.children) > 1
    return is_join(planTree.parent) or planTree.get_attr("Parent Relationship") == "InitPlan" or planTree.get_attr("Parent Relationship") == "SubPlan"
