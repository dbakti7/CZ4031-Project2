#from plan_parser import PlanParser
from json_parser import JsonParser
from json_parser import fill_leaves_data

jsonParser = JsonParser("plans/query7.json")
root = jsonParser.get_tree()
fill_leaves_data(root, False)

# Samples usage
#print(root.attributes) # list all attributes

# Sample usage of get_attr function to get a value of an attribue
#print(root.get_attr("Node Type"))
#print(root.get_attr("RandomAttr")) # Non existing attribute will return ""
#print(root.children[0].get_attr("Total Cost"))

# Explain still can be invoked with the same way, note the lower case of "explain"
print(root.explain())
