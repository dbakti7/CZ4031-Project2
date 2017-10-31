import re
def hashJoin(planTree):
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

'''
#hash join definition
from collections import defaultdict
 
def hashJoin(table1, index1, table2, index2):
    h = defaultdict(list)
    # hash phase
    for s in table1:
        h[s[index1]].append(s)
    # join phase
    return [(s, r) for r in table2 for s in h[r[index2]]]
'''
