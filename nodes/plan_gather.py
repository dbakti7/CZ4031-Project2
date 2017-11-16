from utils import *

# Node Type: Gather

def gather(tree):
    msg = ""
    if (is_branch(tree)):
        msg += ". "
        return msg
    return msg + tree.parent.explain()

# Node Type: Gather Merge

def gather_merge(tree):
    msg = ""
    if (is_branch(tree)):
        msg += ". "
        return msg
    return msg + tree.parent.explain()
        
    
