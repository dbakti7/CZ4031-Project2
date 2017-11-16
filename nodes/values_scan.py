def values_scan(planTree):
    node = planTree.get_attr("Node Type")
    values = planTree.get_attr("Alias")
    msg = "The DBMS performs {} on {}".format(node, values)

    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()

