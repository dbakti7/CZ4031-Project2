import re

def regexParser(line):
    '''
    Return: list of 3 elements
    [node_type, column_name, table_name]
    OR
    [node_type, table_name, ""]
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
    
    p = re.compile(pattern, re.X)
    
    res = p.search(line)
    if(res != None):
        return [res.group(1), res.group(3), res.group(5)]
    
    p = re.compile(pattern1, re.X)
    res = p.search(line)
    if(res != None):
        return [res.group(1), res.group(3), ""]
    return ["", "", ""]

# Examples
print(regexParser("Index Scan using person_pkey on person"))
print(regexParser("Seq Scan on pg_class c"))
