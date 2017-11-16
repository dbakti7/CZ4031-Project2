from utils import *

def subquery_scan(planTree):
    node = planTree.get_attr("Node Type")
    subqueryname = planTree.get_attr("Alias")
    msg = "The DBMS performs {} on subquery {}. ".format(node, subqueryname)

    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()
