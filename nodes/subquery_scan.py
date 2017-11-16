from utils import *

def subquery_scan(planTree):
    node = planTree.get_attr("Node Type")
    subquery_name = planTree.get_attr("Alias")
    if subquery_name != '':
        msg = ". This subquery is called {}".format(subquery_name)
    else:
        return '' + planTree.parent.explain()
        
    if (is_branch(planTree)):
        msg += ". "
        return msg

    return msg + planTree.parent.explain()
