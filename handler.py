from query_handler import connect, query_handler
from tts import speak

def handler(payload):
    action_type = payload["type"]
    data = payload["data"]

    if action_type == 0:
        result = connect(data)
        if result:
            return "Connection Successful!"
        else:
            return "Connection Unsuccessful!"
    elif action_type == 1:
        result = query_handler(data)
        return result
    elif action_type == 2:
        print("Explain Plan")
    elif action_type == 3:
        speak(data)
    else:
        print("Type not valid")

    return "Action {} - Data {}".format(action_type, data)
