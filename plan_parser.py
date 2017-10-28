from plan_tree import PlanTree
import re

def RegexParser(line):
    '''
    Return: list of 3 elements
    [node_type, column_name, table_name]
    OR
    [node_type, table_name, ""]
    OR
    OR
    [node_type, "", ""]
    OR
    ["", "", ""]: invalid input
    '''
    nodes = [ ["Seq\sScan", "Index\sScan", "Index\sScan\sBackward",
               "Index\sOnly\sScan", "Bitmap\sIndex\sScan", "Bitmap\sHeap\sScan",
               "BitmapOr", "Function\sScan", "Sort", "Limit", "HashAggregate",
               "Hash\sJoin", "Hash", "Nested\sLoop", "Merge\sJoin",
               "Hash\sLeft\sJoin", "Hash\sRight\sJoin", "Merge\sLeft\sJoin",
               "Merge\sRight\sJoin", "Nested\sLoop\sLeft\sJoin",
               "Hash\sFull\sJoin", "Merge\sFull\sJoin", "Hash\sAnti\sJoin",
               "Merge\sAnti\sJoin", "Nested\sLoop\sAnti\sJoin", "Materialize",
               "Unique", "Append", "Result", "Values\sScan", "GroupAggregate",
               "HashSetOp", "CTE\sScan", "InitPlan","SubPlan"] ]
    keywords = [ ['on', 'using'] ]


    nodes = ['|'.join(x) for x in nodes]
    keywords = ['|'.join(x) for x in keywords]
    
    pattern = r'\b ({}) \s+ ({}) \s+ (.*) ({}) \s+ (.*)\b'.format(*nodes, *keywords, *keywords)
    pattern1 = r'\b ({}) \s+ ({})\s+ (.*) \b'.format(*nodes, *keywords)
    pattern2 = r'\b ({}) \b'.format(*nodes)
    
    p = re.compile(pattern, re.X)
    
    res = p.search(line)
    if(res != None):
        return [res.group(1), res.group(3), res.group(5)]
    
    p = re.compile(pattern1, re.X)
    res = p.search(line)
    if(res != None):
        return [res.group(1), res.group(3), ""]

    p = re.compile(pattern2, re.X)
    res = p.search(line)
    if(res != None):
        return [res.group(1), "", ""]
    return ["", "", ""]



class PlanParser(object):
    def __init__(self, fileName):
        self.fileName = fileName
    
    def leadingSpaces(self, string):
        spaces = len(string) - len(string.lstrip())
        if(string.lstrip()[0] == '-'):
            return spaces + 2 + self.leadingSpaces(string[spaces + 2:])
        else:
            return spaces

    def getLevel(self, string):
        spaces = self.leadingSpaces(string)
        if(spaces == 0):
            return -1
        if((spaces - 1) % 6 == 0): # new level
            return int(((spaces - 1) / 6) * 2)
        else: # params of a level: (spaces - 3) % 6 == 0
            return int(((spaces - 3) / 6) * 2 + 1)

    def getCostData(self, string):
        costIndex1 = string.find("cost=")
        costIndex2 = string.find("..")
        rowsIndex = string.find("rows=")
        widthIndex = string.find("width=")
        return float(string[costIndex1+5: costIndex2]), \
               float(string[costIndex2+2: rowsIndex-1]), \
               int(string[rowsIndex+5: widthIndex-1]), \
               int(string[widthIndex+6:string.rfind(")")])
    def cleanData(self, string):
        string = string.lstrip()
        costIndex = string.find("(cost=")
        if(costIndex != -1):
            pass
        else:
            costIndex = len(string)
        if(string[0] == '-'):
            return string[4:costIndex], string[costIndex:]
        return string[:costIndex], string[costIndex:]

    def getTree(self):
        with open(self.fileName) as f:
            plan = f.readlines()
            # Line 0 is header
            # Line 1 is separator
            # Line -1 is total rows


        root = PlanTree()
        currentNode = root
        cleanString, costString = self.cleanData(plan[2])
        currentNode.data = cleanString
        attr = RegexParser(currentNode.data)
        if(attr[2] != ""):
            currentNode.node, currentNode.column, currentNode.table = attr[0], attr[1], attr[2]
        elif(attr[1] != ""):
            currentNode.node, currentNode.table = attr[0], attr[1]
        elif(attr[0] != ""):
            currentNode.node = attr[0]
                    
        currentNode.cost1, currentNode.cost2, currentNode.rows, currentNode.width = \
                           self.getCostData(costString)
        currentLevel = 0
        for i in range(3, len(plan)):
            
            level = self.getLevel(plan[i])
            if(level == -1):
                break
            if(level > currentLevel and level % 2 == 0):
                currentLevel = level
                currentNode.children.append(PlanTree())
                currentNode.children[-1].parent = currentNode
                currentNode = currentNode.children[-1]
                cleanString, costString = self.cleanData(plan[i])
                currentNode.data = cleanString
                attr = RegexParser(currentNode.data)
                if(attr[2] != ""):
                    currentNode.node, currentNode.column, currentNode.table = attr[0], attr[1], attr[2]
                elif(attr[1] != ""):
                    currentNode.node, currentNode.table = attr[0], attr[1]
                elif(attr[0] != ""):
                    currentNode.node = attr[0]
                currentNode.cost1, currentNode.cost2, currentNode.rows, currentNode.width = \
                           self.getCostData(costString)
            elif(level > currentLevel and level % 2 == 1):
                currentNode.params.append(self.cleanData(plan[i]))
                cleanString, costString = self.cleanData(plan[i])
                currentNode.params.append(cleanString)
            elif(level <= currentLevel and level % 2 == 0):
                while(currentLevel != level):
                    currentLevel -= 2
                    currentNode = currentNode.parent
                    
                currentNode = currentNode.parent
                currentNode.children.append(PlanTree())
                currentNode.children[-1].parent = currentNode
                currentNode = currentNode.children[-1]
                cleanString, costString = self.cleanData(plan[i])
                currentNode.data = cleanString
                attr = RegexParser(currentNode.data)
                if(attr[2] != ""):
                    currentNode.node, currentNode.column, currentNode.table = attr[0], attr[1], attr[2]
                elif(attr[1] != ""):
                    currentNode.node, currentNode.table = attr[0], attr[1]
                elif(attr[0] != ""):
                    currentNode.node = attr[0]
                currentNode.cost1, currentNode.cost2, currentNode.rows, currentNode.width = \
                           self.getCostData(costString)
            
        return root

