import re
def hash_join(planTree):
    regexp = re.compile(r'[aA]nti')
    replanTree.node
    if regexp.search(planTree.node):
        negatonStr = 'not in'
    else:
        negationStr = 'from'
    description = "The DBMS performs {} that loads the candidate records from {} into a hash table which is then probed for each record {} {}".format(
        planTree.node, param1 , negationStr, param2)
    childStr = ""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
