from utils import *

def subquery_scan(planTree):
    node = planTree.get_attr("Node Type")
    subquery_name = planTree.get_attr("Alias")
    description = ''
    if subquery_name != '':
        description = "this subquery is called {}".format(subquery_name)
    
        
    if (is_branch(planTree)):
        return get_conjuction() + description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return get_conjuction() + description + ". "
    return description + ", " + parentString
