from utils import *
def limit(tree):
    plan_rows = tree.get_attr("Plan Rows")
    result = ", then limited to {} rows".format(plan_rows)

    if(is_branch(tree)):
        return result

    return result + planTree.parent.explain()
