from utils import *

def unique(planTree):
    description = "eliminate the duplicate values"

    if(is_branch(planTree)):
        return description + ". "

    parentString = planTree.parent.explain()
    if(parentString == ""):
        return description + ". "
    if(planTree.parent != None and is_branch(planTree.parent)):
        return description + ", " + get_conjuction() + parentString
    return description + ", " + parentString

