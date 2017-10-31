# Andre's imports
from hash_join import hashJoin
from Hash import Hash
from nested_loop import nestedLoop
from merge_join import mergeJoin
from values_scan import valuesScan
# Dian's imports
from sort_node import Sort

# JM's imports


# ND's imports


# import your functions above
# the function must use the following signature:
# def function_name(planTree):
# you can access all the object elements with planTree.attribute_name
# Add it into the dictionary below, with entry: node_name_query_plan: function_name

functionList ={
    # Note: Always end your section with comma
    # Dian's functions
    'Sort': Sort,

    # ND's functions
    

    # JM's functions
    

    # Andre's functions
    'Hash\sJoin' : hashJoin,
    'Hash\sLeft\sJoin' : hashJoin,
    'Hash\sRight\sJoin' : hashJoin,
    'Hash\sFull\sJoin' : hashJoin,
    'Hash\sAnti\sJoin' : hashJoin,

    'Hash' : Hash,
    'Nested\sLoop' : nestedLoop ,
    'Merge\sJoin':  mergeJoin,
    'Merge\sLeft\sJoin' : mergeJoin,
    'Merge\sRight\sJoin' : mergeJoin,
    'Merge\sFull\sJoin' : mergeJoin,
    'Merge\sAnti\sJoin' : mergeJoin,
    'Values\sScan' : valuesScan,
    }

class PlanTree(object):
    def __init__(self):
        self.data = None
        self.node = None
        self.on = None
        self.using = None
        self.parent = None
        self.children = []
        self.params = []
        self.cost1 = 0
        self.cost2 = 0
        self.rows = 0
        self.width = 0
    
    def Explain(self):
        return functionList[self.node](self)
        
