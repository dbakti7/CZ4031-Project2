from utils import is_scan_node
from utils import is_join
from utils import get_conjuction
def limit(planTree):
    operation_name = planTree.get_attr("Node Type")
    plan_rows = planTree.get_attr("Plan Rows")
    actual_rows = planTree.get_attr("Actual Rows")
    msg = ""
    for child in planTree.children:
        msg += child.explain()
        msg += ", "
        if(is_scan_node(child)):
            msg += "then "
        elif(is_join(planTree.parent)):
            msg += get_conjuction()
    #msg = "The DBMS performs {}, which cuts down the number of rows to the top {} rows. As a result, the table now have only {} rows.".format(operation_name, plan_rows, actual_rows)
    msg += " the results are limited to the top {} rows. ".format(plan_rows)
    return msg
