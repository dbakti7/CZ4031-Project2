from utils import *
def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    #description = "The DBMS performs {} function that maps all the set of search-keys {} to the address where actual records are placed.".format(
        #node, key)
    #childStr =""
    description = ""
    if(is_scan_node(planTree.children[0])):
        description += ", then "
    # elif(is_join(planTree.parent) and not (is_join(planTree.children[0]) or (len(planTree.children) > 1 and is_join(planTree.children[1])))):
    #     childStr += get_conjuction()
    description += "hashed"

    if(is_branch(planTree)):
        return description + ". "
    return description + planTree.parent.explain()
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
