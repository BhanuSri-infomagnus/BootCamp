import pyodbc  # Importing the pyodbc library to interact with the SQL Server database

# Connection string to connect to the SQL Server database (replace with your own details)
conn_str = (
    "DRIVER=SQL Server;"                # SQL Server ODBC driver
    "SERVER=DESKTOP-OK8NL61\\SQLEXPRESS;"  # Server name and instance
    "DATABASE=AdventureWorksDW2022;"      # Database name
    "UID=Bhanu;"                         # Username for authentication
    "PWD=admin"                          # Password for authentication
)

# Establish the connection to the database using the connection string
conn = pyodbc.connect(conn_str)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to count the number of distinct EmployeeKey values in the DimEmployee table
cursor.execute("SELECT count(distinct EmployeeKey) FROM DimEmployee")
# Fetch and print the result (which will be a single row with the count of unique EmployeeKey values)
for row in cursor.fetchall():
    print(row)

# Execute a query to count the distinct EmployeeKey values grouped by gender
cursor.execute("SELECT gender, count(distinct EmployeeKey) FROM DimEmployee GROUP BY gender")
# Fetch and print the results (showing the number of distinct employees for each gender)
for row in cursor.fetchall():
    print(row)

# Execute a query to count the distinct EmployeeKey values where the employee's status is 'current'
cursor.execute("SELECT count(distinct EmployeeKey) FROM DimEmployee WHERE Status='current'")
# Fetch and print the result (this will give the number of distinct employees who are currently active)
for row in cursor.fetchall():
    print(row)

# Execute a query to retrieve the top 10 employees' full names (concatenating FirstName and LastName)
cursor.execute("SELECT TOP 10 concat(FirstName, LastName) FROM DimEmployee")
# Fetch and print the results (this will display the first and last names of the first 10 employees)
for row in cursor.fetchall():
    print(row)

# Execute a query to retrieve the names of employees and their managers by joining the DimEmployee table to itself
cursor.execute("""
    SELECT a.EmployeeFullName as Employee, b.EmployeeFullName as Manager
    FROM DimEmployee as a
    JOIN DimEmployee as b ON a.ParentEmployeeKey = b.EmployeeKey
""")
# Fetch and print the results (this will list employees and their respective managers)
for row in cursor.fetchall():
    print(row)

# Close the connection to the database once all queries are executed
conn.close()
