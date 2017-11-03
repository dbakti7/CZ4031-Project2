def hash_node(planTree):
    node = planTree.get_attr("Node Type")
    key = planTree.get_attr("Hash Cond")
    description = "The DBMS performs {} function that maps all the set of search-keys {} to the address where actual records are placed.".format(
        node, key)
    childStr =""
    for child in planTree.children:
        childStr += child.explain()
    return description + childStr
