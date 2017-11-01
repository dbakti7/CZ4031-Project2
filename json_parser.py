from plan_tree import PlanTree
import json

class JsonParser(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.jsonData = None

    def get_json(self, lines):
        # hacky cleaning approach here, TODO: Please fix, maybe.

        # removing headers
        for i in range(len(lines)):
            if('[' in lines[i]):
                lines = lines[i:]
                break

        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

            # trailing empty lines
            if(lines[i] == ""):
                continue

            # detecting "number of rows" information, if any
            if("row)" in lines[i]):
                lines = lines[:i]
                break

            # removing '+' char, if any
            if(lines[i][-1] == '+'):
                lines[i] = lines[i][:-1]
                lines[i] = lines[i].rstrip()
            
        self.jsonData = json.loads(' '.join(lines))

    def get_attributes(self, data, node):
        for datum in data.items():
            if(datum[0] == "Plans"):
                continue
            node.attributes[datum[0]] = datum[1]

    def get_children_data(self, data, node):
        if("Plans" not in data):
            return
        for plan in data["Plans"]:
            childNode = PlanTree()
            childNode.parent = node
            self.get_attributes(plan, childNode)
            self.get_children_data(plan, childNode)
            node.children.append(childNode)


    def get_tree(self):
        with open(self.fileName) as f:
            lines = f.readlines()
            self.get_json(lines)
        
        # TODO: investigate if it is possible to have more than one root level nodes
        root = PlanTree()
        self.get_attributes(self.jsonData[0]["Plan"], root)
        self.get_children_data(self.jsonData[0]["Plan"], root)
        
        return root
        
        
