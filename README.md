# SQL Server Python Connector
# Description
This project demonstrates how to connect to a SQL Server database using Python and the pyodbc library. It includes Python code for setting up a connection to a database and executing various SQL queries.

# Features
Connect to SQL Server databases using Python.
Execute queries to fetch and manipulate data.
Includes connection configuration and sample queries for employees.

# Installation
# Prerequisites

SQL Server ODBC driver installed on your machine (check your SQL Server version for the appropriate driver).
Python 3.13.3
SQL Server running locally or remotely
ODBC Driver 17 (or 18) for SQL Server
Python Libraries:
pyodbc
python-dotenv

# Step-by-Step Instructions
Clone the repository:

git clone https://github.com/BhanuSri-infomagnus/Bootcamp.git

# Set up a virtual environment:

Windows:

python -m venv venv

macOS/Linux:

python3 -m venv venv

# Activate the virtual environment:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

# Install dependencies:
After activating the virtual environment, install the required libraries:

pip install -r requirements.txt

# Configure Database Connection:

Update the sql_connection.py file with your SQL Server credentials, such as server name, database name, username, and password.

# Run the code:
After setting up the environment and configuring the connection, run the script to test the connection:

python sql_connection.py

# Usage
Example Code: sql_connection.py

import pyodbc

# Set up the database connection
conn = pyodbc.connect(
    'DRIVER={SQL Server};' 
    'SERVER=your_server_name;'
    'DATABASE=AdventureWorksDW2022;'
    'UID=your_username;'
    'PWD=your_password'
)

cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM DimEmployee")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
Expected Output:

A list of records from the DimEmployee table will be displayed.

# Requirements
The following libraries are required for this project:

pyodbc: Python ODBC interface for connecting to SQL databases.

You can install them by running:

pip install -r requirements.txt

## 📝 Setup .env File

1. Copy the `.env.example` file and rename it to `.env`.

2. Open the `.env` file and replace the placeholders with your actual SQL Server connection details.

Example:

UID=your_sql_username
password_value=your_sql_password
SERVER=localhost\SQLEXPRESS
DATABASE=AdventureWorksDW2022


# .gitignore Example
This repository contains a .gitignore file to ensure that unnecessary files, such as the virtual environment, are not committed to the Git repository.

# How to Customize
Update your connection details: Replace the placeholders (your_server_name, your_username, your_password) with actual values to connect to your SQL Server instance.
