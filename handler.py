import json
from query_handler import connect, query_handler
from index import explain

"""
    Message type:
    0: Check Connection
    1: Explain Query Execution Plan; Input: Query
    2: Explain Query Execution Plan; Input: Plan
    3: Text to speech
"""

def handler(payload):
    action_type = payload["type"]
    data = payload["data"]

    if action_type == 0:
        result = connect(data)
        if result:
            return "Connection Successful!"
        else:
            return "Unable to establish connection to the database, Please check your credentials!"

    elif action_type == 1:
        result = query_handler(data)
        return result

    elif action_type == 2:
        try:
            json.loads(data)
        except Exception as err:
            print(err)
            return "Please enter a valid JSON format!"

        return explain(plan=json.loads(data))
    elif action_type == 3:
        filename = "plans/query{}.json".format(data)
        return explain(filename=filename)
            
    else:
        print("Type not valid")
