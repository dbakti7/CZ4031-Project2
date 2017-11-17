import re

from utils import is_join
from utils import is_scan_node
from utils import is_branch

from cond_parser import cond_parser

from nodes.scan import *
from nodes.join import *
from nodes.others import *

filters = ["Filter", "Hash Cond", "Index Cond", "Merge Cond", "Recheck Cond", "Join Filter", "Sort Key", "Group Key", "Output"]

functionList ={
    'Sort': sort,
    'Aggregate': aggregate,
    'Materialize': materialize,
    'Limit': limit,
    'Hash Join': hash_join,
    'Result' : result,
    'Function Scan': function_scan,
    'Gather': gather,
    'Gather Merge': gather,
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
    'Hash' : hash_node,
    'Nested Loop' : nested_loop ,
    'Merge Join':  merge_join,
    'Values Scan' : values_scan,
    'Subquery Scan' : subquery_scan,
    }

class PlanNode(object):
    """
        Data Structure to represent a node in query execution tree
    """
    def __init__(self):
        self.parent = None
        self.children = []
        self.attributes = {}
        self.nodeNumber = 0

    def explain(self):
        """
        Call the respective node function to get the explanation
        """
        node = self.attributes["Node Type"]

        # handling unknown node
        if node not in functionList:
            return node

        return functionList[node](self)
        
    def get_attr(self, attr):
        """
        Get attribute values of a node, empty string if not exist
        """
        if attr not in self.attributes:
            return ""
        return self.attributes[attr]

    def get_leaf(self):
        """
        Get the leaf node of current subtree
        """
        num = 0
        if(len(self.children) == 0):
            return self.nodeNumber
        for child in self.children:
            current = child.get_leaf()
            if(current > num and current - num > 1):
                num = current
        return num

    def get_branching_point(self):
        """
        Get the lowest branching point (ancestor with more than one child nodes).
        """
        if(is_branch(self)):
            return self
        return self.parent.get_branching_point()
    
    def replacePlaceHolders(self, mapper):
        """
        Preprocessing function into more readable form
        """
        for filter in filters:
            attr = self.get_attr(filter)
            if(attr == ""):
                continue
            if(type(attr) is list):
                for i in range(len(attr)):
                    temp = attr[i]
                    for key, value in mapper["Subplan Results"].items():
                        self.attributes[filter][i] = temp.replace(key, value)
                    self.attributes[filter][i] = cond_parser(self.attributes[filter][i])
            else:
                for key, value in mapper["Subplan Results"].items():
                    self.attributes[filter] = attr.replace(key, value)
                self.attributes[filter] = cond_parser(self.attributes[filter])
        for child in self.children:
            child.replacePlaceHolders(mapper)

    def traverse(self, number, mapper, alias, subplan):      
        """
        Recursive function to traverse the tree, assigning node index and identifying
        InitPlan and SubPlan nodes
        """
        if(is_scan_node(self)):  
            self.nodeNumber = number
            if(subplan != ""):
                mapper[subplan][number] = self
            else:
                mapper[number] = self
            
            # handle alias if this is a subquery scan
            if(alias != ""):
                self.attributes["Alias"] = alias
            return number
        elif(is_join(self)):
            self.nodeNumber = number
            if(subplan != ""):
                mapper[subplan][number] = self
            else:
                mapper[number] = self
            nextNumber = 2 * number + 1
            maxNum = -1
            for child in self.children:
                num = child.traverse(nextNumber, mapper, alias, subplan)
                nextNumber += 1
                if(num - maxNum > 1): # we prefer left node
                    maxNum = num
            return maxNum
        else:
            # handling alias in subquery
            if(self.get_attr("Alias") != ""):
                alias = self.get_attr("Alias")
            if(len(self.children) == 0):
                self.nodeNumber = number
                if(subplan != ""):
                    mapper[subplan][number] = self
                else:
                    mapper[number] = self
                return number
            if(len(self.children) == 1):
                parentRelationship = self.get_attr("Parent Relationship")
                if(parentRelationship == "InitPlan"):
                    result = re.search("\$\d+", self.get_attr("Subplan Name"))
                    if(result):
                        ot = self.get_attr("Output")
                        if(ot == ""):
                            ot = ["result of InitPlan"]
                        if(re.search("\$\d+", ot[0])):
                            ot = ["result of InitPlan"]
                        mapper["Subplan Results"][result.group()] = ot[0]
                    return self.children[0].traverse(len(mapper["InitPlan"]), mapper, alias, "InitPlan")
                elif(parentRelationship == "SubPlan"):
                    result = self.get_attr("Subplan Name")
                    if(result):   
                        mapper["Subplan Results"][result] = result
                    return self.children[0].traverse(len(mapper["SubPlan"]), mapper, alias, "SubPlan")
                return self.children[0].traverse(number, mapper, alias, subplan)
            else:
                self.nodeNumber = number
                if(subplan != ""):
                    mapper[subplan][number] = self
                else:
                    mapper[number] = self
                maxNum = -1
                for child in self.children:
                    num = child.traverse(number, mapper, alias, subplan)
                    if(num - maxNum > 1): # we prefer left node
                        maxNum = num
                return maxNum
    
