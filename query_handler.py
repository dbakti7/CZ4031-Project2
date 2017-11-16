import psycopg2
import json
from index import explain

def connect(data):
    db_name = data["db_name"]
    user = data["user"]
    password = data["password"] 
    host = data["host"]
    port = data["port"]

    try:
        conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
        return conn
    except Exception as err:
        print(err)
        return ""

def query_handler(data):
    query = "explain (format json) {}".format(data["query"])
    conn = connect(data)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        plan = cursor.fetchall()
    except Exception as err:
        print(err)
        return "Error when executing query! Please check your syntax"

    return explain(plan[0][0])

# data = {
#         "query": "explain (format json) select * from authored limit 10;",
#         "db_name": "CZ4031",
#         "user": "postgres",
#         "password": "admin",
#         "host": "localhost",
#         "port": "5432"
# }
#
# query_handler(data)

