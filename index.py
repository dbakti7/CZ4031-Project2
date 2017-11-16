#from plan_parser import PlanParser
from json_parser import JsonParser
from utils import *
plans = ["query2_1", "query1", "query2", "query3a", "query3b", "query3c", "query4a", "query4b", "query5", "query6", "query7", "query8", "query9a", "query9b", "query10", "union", "values_scan", "extreme"]
for plan in plans:
    jsonParser = JsonParser("plans/" + plan + ".json")
    print(plan)
    print("-------------------------------------------------")
    root = jsonParser.get_tree()
    mapper = {"Subplan Results": {}, "InitPlan": {}, "SubPlan": {}}
    num, node = root.traverse(0, mapper, "")
    root.replacePlaceHolders(mapper)
    # num contains biggest traverse index
    # node contains the node

    counter = 0
    def get_explanation(startIndex, rootNumber, intermediate=""):
        current= startIndex
        while(current != rootNumber):
            if(current % 2):
                sibling = current + 1
            else:
                sibling = current - 1
            subject = "This "
            
            if(is_join(mapper[current])):
                if(not is_join(mapper[current].parent)):
                    print("The " + mapper[current].get_attr("Node Type") + " operation results will be ", end='')
                    print(mapper[current].parent.explain())
            else:
                print(mapper[current].explain(), end='')

            if(is_join(mapper[current]) and is_join(mapper[sibling])):
                print("Let's call this intermediate result as A.")
                subject = "A "
                get_explanation(mapper[sibling].get_leaf(), sibling, "A")
                
            else:
                string = subject + "will be the " + mapper[current].get_branching_point().get_attr("Parent Relationship") + " relation of " + mapper[(current - 1) // 2].explain() + " with table "
                if(mapper[sibling].get_attr("Alias") != ""):
                    string += mapper[sibling].get_attr("Alias") + ". " + mapper[sibling].get_attr("Alias") + " is retrieved with "
                else:
                    string += mapper[sibling].get_attr("Relation Name") + " table. " + mapper[sibling].get_attr("Relation Name") + " is retrieved with "
                string += mapper[sibling].explain()
                print(string)
            current = (current - 1) // 2
        if(rootNumber != 0):
            print(mapper[current].explain())
            print("Let's call this intermediate result as B.")
            print("B will be the " + mapper[current].get_branching_point().get_attr("Parent Relationship") + " relation of "
            + mapper[(current - 1) // 2].get_attr("Node Type") + " with intermediate result " + intermediate + ". ")
        elif(is_join(mapper[current])):
            if(mapper[current].parent != None):
                print("The " + mapper[current].get_attr("Node Type") + " operation results will be ", end='')
                print(mapper[current].parent.explain())
        # single node like Alias, which is not join, so still need to be explained
        else:
            print(mapper[current].explain())
        # if(counter == 2):
        #     break

    if(len(mapper["InitPlan"]) > 0 or len(mapper["SubPlan"]) > 0):
        print("First, ", end='')
        for k in mapper["InitPlan"].keys():
            print(mapper["InitPlan"][k].explain())
        for k in mapper["SubPlan"].keys():
            print(mapper["SubPlan"][k].explain())

    get_explanation(num, 0)
    print()
    print()
    print()
    #print(mapper[num + 1].explain())
    # Samples usage
    #print(root.attributes) # list all attributes

    # Sample usage of get_attr function to get a value of an attribue
    #print(root.get_attr("Node Type"))
    #print(root.get_attr("RandomAttr")) # Non existing attribute will return ""
    #print(root.children[0].get_attr("Total Cost"))

    # Explain still can be invoked with the same way, note the lower case of "explain"
    # print(root.explain())
