import pyodbc
import os
from dotenv import load_dotenv

class DatabaseConnector:
    def __init__(self, env_file=".env"):
        """Initialize connection using environment variables"""
        # Load environment variables from .env file
        load_dotenv(env_file)
        
        # Get connection details from environment
        self.server = os.getenv("SERVER")
        self.database = os.getenv("DATABASE")
        self.username = os.getenv("UID")
        self.password = os.getenv("password_value")
        
        # Validate all required environment variables are set
        if not all([self.server, self.database, self.username, self.password]):
            raise ValueError("Missing required database connection parameters in environment")
            
        # Establish connection
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        self.cursor = self.conn.cursor()
    
    def execute_query(self, query, params=None):
        """Execute a SQL query with optional parameters"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Query execution error: {e}")
            self.conn.rollback()
            return False
    
    def fetch_data(self, query, params=None):
        """Execute a query and fetch all results"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Data fetch error: {e}")
            return None
    
    def close(self):
        """Close database connection"""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()