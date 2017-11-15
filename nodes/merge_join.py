import re
def merge_join(planTree):
    msg = ""
    for i in range (len(planTree.children)):
        child = planTree.children[i]
        if(planTree.isRightLeaf):
            if(i == 0):
                if(planTree.leftLeaf[0] == "Scan"):
                    msg += "On the left side (hahha) we perform "
            elif(planTree.rightLeaf[0] == "Scan"):
                msg += "After that, we perform "
        msg += child.explain()
        if(not planTree.isRightLeaf):
            if(i == 0):
                msg += "This will be merge joined with "
                if(planTree.rightLeaf[0] == "Join"):
                    msg += "the result of join operation between " + planTree.rightLeaf[1][0] + " and " + planTree.rightLeaf[1][1] + ". "
                else:
                    msg += str(planTree.rightLeaf[1]) + ". "
            else:
                msg += "This join result will be the right hand side to be merge joined with " + planTree.leftLeaf[1] + " table. "
    return msg

    node = planTree.get_attr("Node Type")
    regexp = re.compile(r'[aA]nti')
    condition = planTree.get_attr("Merge Cond")
    if regexp.search(node):
        negatonStr = 'not in'
    else:
        negationStr = 'from'
    description = "The DBMS performs {} on two sorted lists with condition {}.".format(
        node, condition )
    childStr = ""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
