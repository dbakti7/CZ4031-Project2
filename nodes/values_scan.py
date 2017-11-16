from utils import *
def values_scan(planTree):
    node = planTree.get_attr("Node Type")
    values = planTree.get_attr("Alias")
    msg = "{} on {}".format(node, values)

    if (is_branch(planTree)):
        msg += ". "
        return msg

    parentString = tree.parent.explain()
    if(parentString == ""):
        return msg + ". "
    return msg + ", then it will be " + parentString

