# Bootcamp
SQL Server Query Script

This Python script connects to a SQL Server database (AdventureWorksDW2022) using pyodbc and performs some basic SQL queries on the DimEmployee table.

Requirements
Python 3.6+: Install Python from python.org.

pyodbc: Python library for SQL Server connection.

SQL Server ODBC Driver: Required to connect Python to SQL Server.

Install Dependencies
To install the required Python package (pyodbc), run the following command:

pip install pyodbc
Install SQL Server ODBC Driver
You also need the SQL Server ODBC Driver to connect to the database.

On Windows: Download SQL Server ODBC Driver

On Linux/macOS: Follow installation guide

Setup
Clone the repository:

git clone https://github.com/BhanuSri-infomagnus/Bootcamp.git

Configure the database connection:

Open the script and replace the following with your own database details:

conn_str = (
    "DRIVER=SQL Server;"
    "SERVER=your-server-name;"   # Replace with your server name
    "DATABASE=your-databasename;"   # Database name
    "UID=your-username;"         # SQL Server username
    "PWD=your-password"          # SQL Server password
)

Running the Script
After setting up, run the script with:

python yourscript.py