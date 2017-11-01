# Andre's imports


# Dian's imports
from sort_node import sort

# JM's imports
from seq_scan import seq_scan
from index_scan import index_scan
from bitmap import bitmap
from cte_scan import cte_scan

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
    'Seq Scan': seq_scan,
    'Index Scan': index_scan,
    'Index Scan Backward': index_scan,
    'Index Only Scan': index_scan,
    'Index Only Scan Backward': index_scan,
    'BitmapAnd': bitmap,
    'BitmapOr': bitmap,
    'Bitmap Heap Scan': bitmap,
    'Bitmap Index Scan': bitmap,
    'CTE Scan': cte_scan,


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
