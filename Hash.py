def Hash(planTree):
    param = planTree.params[0]
    description = "A hash function that maps all the set of search-keys {} to the address where actual records are placed.".format(
        param)
    childStr =""
    for child in planTree.children:
        childStr += child.Explain() + " "
    return description + " " +childStr
