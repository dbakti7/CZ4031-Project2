def mergeJoin(planTree):
    regexp = re.compile(r'[aA]nti')
    replanTree.node
    if regexp.search(planTree.node):
        negatonStr = 'not in'
    else:
        negationStr = 'from'
    description = "The DBMS performs {} from {} and {} {}, which are both sorted lists.".format(
        planTree.node, list1 , negationStr, list2)
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
