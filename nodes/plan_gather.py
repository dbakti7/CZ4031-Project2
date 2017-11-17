from utils import *

# Node Type: Gather

def gather(planNode):
    description = ""
    if (is_branch(planNode)):
        description += ". "
        return description
    return description + planNode.parent.explain()

# Node Type: Gather Merge

def gather_merge(planNode):
    description = ""
    if (is_branch(planNode)):
        description += ". "
        return description
    return description + planNode.parent.explain()
        
    
