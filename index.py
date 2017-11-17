from json_parser import JsonParser
from utils import *
from nodes.plan_cost import get_execution_cost
plans = ["query2_1", "query1", "query2", "query3a", "query3b", "query3c", "query4a", "query4b", "query5", "query6", "query7", "query8", "query9a", "query9b", "query10", "union", "values_scan", "extreme"]


def get_explanation(mapper, startIndex, rootNumber, intermediate=""):
    result = ""
    current= startIndex
    while(current != rootNumber):
        if(current % 2):
            sibling = current + 1
        else:
            sibling = current - 1
        subject = "This "
        
        if(is_join(mapper[current])):
            if(not is_join(mapper[current].parent)):
                result += "The " + mapper[current].get_attr("Node Type") + " operation results will be "
                result += mapper[current].parent.explain()
        else:
            result += mapper[current].explain()

        if(is_join(mapper[current]) and is_join(mapper[sibling])):
            result += "Let's call this intermediate result as A."
            subject = "A "
            result += get_explanation(mapper, mapper[sibling].get_leaf(), sibling, "A")
            
        else:
            string = subject + "will be the " + mapper[current].get_branching_point().get_attr("Parent Relationship") + " relation of " + mapper[(current - 1) // 2].explain() + " with table "
            if(mapper[sibling].get_attr("Alias") != ""):
                string += mapper[sibling].get_attr("Alias") + ". " + mapper[sibling].get_attr("Alias") + " is retrieved with "
            else:
                string += mapper[sibling].get_attr("Relation Name") + " table. " + mapper[sibling].get_attr("Relation Name") + " is retrieved with "
            string += mapper[sibling].explain()
            result += string
        current = (current - 1) // 2

    if(rootNumber != 0):
        result += mapper[current].explain()
        result += "Let's call this intermediate result as B."
        result += "B will be the " + mapper[current].get_branching_point().get_attr("Parent Relationship") + \
        " relation of " + mapper[(current - 1) // 2].get_attr("Node Type") + \
        " with intermediate result " + intermediate + ". "
    elif(is_join(mapper[current])):
        if(mapper[current].parent != None):
            result += "The " + mapper[current].get_attr("Node Type") + " operation results will be "
            result += mapper[current].parent.explain()
    # single node like Alias, which is not join, so still need to be explained
    else:
        result += mapper[current].explain()
    return result

def get_explain_string(root):
    mapper = {"Subplan Results": {}, "InitPlan": {}, "SubPlan": {}}
    num, node = root.traverse(0, mapper, "")
    root.replacePlaceHolders(mapper)

    result = ""
    if(len(mapper["InitPlan"]) > 0 or len(mapper["SubPlan"]) > 0):
        result += "First, "
        for k in mapper["InitPlan"].keys():
            result += mapper["InitPlan"][k].explain()
        for k in mapper["SubPlan"].keys():
            result += mapper["SubPlan"][k].explain()

    result += get_explanation(mapper, num, 0)
    result += get_execution_cost(root)
    return result

def explain(plan):
    jsonParser = JsonParser(None)
    try:
        root = jsonParser.get_tree(plan)
    except Exception as err:
        print(err)
        return "The query plan you entered is not valid!"
    return get_explain_string(root)

# for plan in plans:
#     jsonParser = JsonParser("plans/" + plan + ".json")
#     print(plan)
#     print("-------------------------------------------------")
#     root = jsonParser.get_tree()
#     print(get_explain_string(root))
#     # num contains biggest traverse index
#     # node contains the node  
#     
#     print()
#     print()
#     print()
