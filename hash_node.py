def hash_node(planTree):
    print(planTree.params)
    description = "A hash function that maps all the set of search-keys {} to the address where actual records are placed.".format(
        planTree.params)
    childStr =""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
