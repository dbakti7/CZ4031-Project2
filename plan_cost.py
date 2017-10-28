from plan_tree import PlanTree

# cost1 = time taken for 1st row
# cost2 = time taken for all rows

class PlanCost(object):
    def getCost (self):
        one_cost = self.data + "- Cost of execution of first row : "+ str(self.cost1)
        all_cost = self.data + "- Cost of execution of all rows : "+ str(self.cost2)
        rows = self.data + "- Total row execution : "+ str(self.rows)
        width = self.data + "- Total row width : "+ str(self.width)
        return all_cost
        #print(one_cost)
        #print(all_cost)
        #print(rows)
        #print(width)

    
    
