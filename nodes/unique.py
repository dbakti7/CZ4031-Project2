from utils import *

def unique(tree):
    msg = "Remove duplicate values"

    if (is_branch(tree)):
        msg += ". "
        return msg

    return msg + tree.parent.explain()

