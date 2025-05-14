import pyodbc

class DatabaseConnector:
    def __init__(self, server, database, username, password):
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};DATABASE={database};'
            f'UID={username};PWD={password}'
        )
        self.cursor = self.conn.cursor()
    
    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()