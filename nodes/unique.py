from utils import *

def unique(planTree):
    result = ""

    if (is_branch(planTree)):
        result += " and then eliminate the duplicate values"
        return result + ". "
    else:
        result += ", eliminate the duplicate values"

    return result + planTree.parent.explain()

