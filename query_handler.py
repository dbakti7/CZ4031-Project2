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
        return ""

def query_handler(data):
    query = data["query"]
    conn = connect(data)
    cursor = conn.cursor()
    cursor.execute(query)
    plan = cursor.fetchall()
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
#
