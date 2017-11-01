from plan_parser import PlanParser
from json_parser import JsonParser
from plan_cost import PlanCost

jsonParser = JsonParser("json2.json")
root = jsonParser.get_tree()

# Samples usage
print(root.attributes) # list all attributes
print(root.attributes["Node Type"])
print(root.children[0].attributes["Total Cost"])

# Explain still can be invoked with the same way, note the lower case of "explain"
#print(root.explain())