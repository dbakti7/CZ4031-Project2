from sort_node import Sort

# import your functions above
# the function must use the following signature:
# def function_name(planTree):
# you can access all the object elements with planTree.attribute_name
# Add it into the dictionary below, with entry: node_name_query_plan: function_name

functionList = {'Nested Loop': NestedLoop, 'GroupAggregate': GroupAggregate, 'Sort': Sort}

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
        
