from plan_parser import PlanParser
from plan_cost import PlanCost


planParser = PlanParser("plan.txt")
root = planParser.getTree()

# Samples usage
print(root.data, root.node)
print(root.children[0].children[0].children[0].children[0].children[0].node)
print(root.children[0].children[0].children[0].children[0].children[0].table)
print(root.children[1].node)
print(root.children[1].table)
print(root.children[1].column)

print(root.params)
print(root.children[0].data, root.children[0].cost1, \
      root.children[0].cost2, root.children[0].rows, \
      root.children[0].width)
print(root.children[1].params)

print(PlanCost.getCost(root))