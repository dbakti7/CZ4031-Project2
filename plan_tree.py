# Andre's imports
from hash_join import hash_join
from hash_node import hash_node
from nested_loop import nested_loop
from merge_join import merge_join
from values_scan import values_scan
from subquery_scan import subquery_scan
# Dian's imports
from nodes import sort
from nodes import aggregate

# JM's imports
from seq_scan import seq_scan
from index_scan import index_scan
from bitmap import bitmap
from cte_scan import cte_scan
from append import append
from unique import unique

# ND's imports
from plan_limit import limit
from plan_hash_join import hash_join
from plan_result import result
from plan_function_scan import function_scan



# import your functions above
# the function must use the following signature:
# def function_name(planTree):
# you can access all the object elements with planTree.attribute_name
# Add it into the dictionary below, with entry: node_name_query_plan: function_name

functionList ={
    # Note: Always end your section with comma
    # Dian's functions
    'Sort': sort,
    'Aggregate': aggregate,

    # ND's functions
    'Limit': limit,
    'Hash Join': hash_join,
    'Result' : result,
    'Function Scan': function_scan,

    # JM's functions
    'Seq Scan': seq_scan,
    'Index Scan': index_scan,
    'Index Only Scan': index_scan,
    'BitmapAnd': bitmap,
    'BitmapOr': bitmap,
    'Bitmap Heap Scan': bitmap,
    'Bitmap Index Scan': bitmap,
    'CTE Scan': cte_scan,
    'Append': append,
    'Unique': unique,


    # Andre's functions
    'Hash' : hash_node,
    'Nested\sLoop' : nested_loop ,
    'Nested\sLoop\sLeft\sJoin' : nested_loop,
    'Nested\sLoop\sAnti\sJoin' : nested_loop,
    'Merge\sJoin':  merge_join,
    'Merge\sLeft\sJoin' : merge_join,
    'Merge\sRight\sJoin' : merge_join,
    'Merge\sFull\sJoin' : merge_join,
    'Merge\sAnti\sJoin' : merge_join,
    'Values\sScan' : values_scan,
    'Subquery Scan' : subquery_scan,
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
