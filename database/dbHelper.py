import sqlite3

class Database:
    def __init__(self, connectionFile):
        self._connFile = connectionFile
        self._result = None

    def executeQuery(self, queryString):
        connection = sqlite3.connect(self._connFile)
        cursor = connection.cursor()

        print("Executing query ...")
        print(queryString)
        
        self._result = cursor.execute(queryString)
        
        connection.commit()
        connection.close()

    def getResult(self):
        return self._result