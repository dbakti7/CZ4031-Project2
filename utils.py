import random
def is_scan_node(planTree):
    node = planTree.get_attr("Node Type")
    
    if(node in ["Seq Scan", "Subquery Scan", "Index Scan", "Bitmap Heap Scan", "Bitmap Index Scan", "Index Only Scan"]):
        return True
    return False

def get_conjuction():
    return random.choice(["and ", "and finally ", "and eventually "])

def is_join(planTree):
    if(planTree == None):
        return True
    if(planTree.get_attr("Node Type") in ["Hash Join", "Merge Join"]):
        return True
    return False
