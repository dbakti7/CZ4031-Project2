# Andre's imports
from hash_join import hash_join
from hash_node import hash_node
from nested_loop import nested_loop
from merge_join import merge_join
from values_scan import values_scan
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
    'Hash\sJoin' : hash_join,
    'Hash\sLeft\sJoin' : hash_join,
    'Hash\sRight\sJoin' : hash_join,
    'Hash\sFull\sJoin' : hash_join,
    'Hash\sAnti\sJoin' : hash_join,

    'Hash' : hash_node,
    'Nested\sLoop' : nested_loop ,
    'Merge\sJoin':  merge_join,
    'Merge\sLeft\sJoin' : merge_join,
    'Merge\sRight\sJoin' : merge_join,
    'Merge\sFull\sJoin' : merge_join,
    'Merge\sAnti\sJoin' : merge_join,
    'Values\sScan' : values_scan,
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
        try:
            return functionList[self.node](self)
        except Exception as err:
            childStr = ''
            for child in self.children:
                childStr += child.Explain()
            return 'Function {} not available. '.format(self.node) + childStr
        
