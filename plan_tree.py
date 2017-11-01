# Andre's imports


# Dian's imports
from sort_node import sort

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
    'Sort': sort,

    # ND's functions
    

    # JM's functions
    

    # Andre's functions
    }

class PlanTree(object):
    def __init__(self):
        self.parent = None
        self.children = []
        self.attributes = {}
    
    def explain(self):
        return functionList[self.attributes["Node Type"]](self)
        
    def get_attr(self, attr):
        if attr not in self.attributes:
            return ""
        return self.attributes[attr]
