class PlanTree(object):
    def __init__(self):
        self.data = None
        self.node = None
        self.table = None
        self.column = None
        self.parent = None
        self.children = []
        self.params = []
        self.cost1 = 0
        self.cost2 = 0
        self.rows = 0
        self.width = 0
        
