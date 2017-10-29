def limit(tree):
    operationName = "Limit"
    limitRows = tree.rows
    tableName = tree.tableName
    msg = "The DBMS performs {} to {} rows on table {}".format(operationName, limitRows, tableName)
    return msg
    
# dummy = {"tableName": "tablename", "rows": "10"}
# print(limit(dummy))
