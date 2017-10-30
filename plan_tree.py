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
        
