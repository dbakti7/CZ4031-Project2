from utils import is_scan_node
from utils import is_join
from utils import get_conjuction

def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    # description = "The DBMS performs {} function that maps all the set of search-keys {} to the address where actual records are placed.".format(
    #     node, key)
    childStr = ""
    #TODO: here we assume it only has one child, please verify and refactor
    for i in range(len(planTree.children)):
        child = planTree.children[i]
        childStr += child.explain()
        if(is_scan_node(child)):
            childStr += ", then "
        elif(is_join(child)):
            childStr += "The join result is then "
        elif(is_join(planTree.parent) and not (is_join(planTree.children[0]) or (len(planTree.children) > 1 and is_join(planTree.children[1])))):
            childStr += get_conjuction()
    # return description + childStr
    childStr += "hashed"
    if(key != ""):
        childStr += " on " + key
    if(is_join(planTree.parent)):
        childStr += ". "
    # if(is_join(planTree.parent) and planTree.isRightLeaf):
    #     childStr += "The results will be joined with " + planTree.parent.leftLeaf[1] + ". "
    return childStr
