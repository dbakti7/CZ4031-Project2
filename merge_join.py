import re
def merge_join(planTree):
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
