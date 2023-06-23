#!/usr/bin/python3

"""
This script lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def list_states_with_n(username, password, database):
 """
Connects to the MySQL server and lists all states with a name starting with 'N'from the specified database.
    Arguments:
        - username: MySQL username
        - password: MySQL password
        - database: Database name
 """
# Connect to the MySQL server
db = MySQLdb.connect(user='MYSQL username', passwd='MYSQL password', db='Database name', host='localhost', port=3306)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

try:
# Execute the query to retrieve states starting with 'N'
 query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
 cursor.execute(query)

# Fetch all the rows returned by the query
 states = cursor.fetchall()

# Print the results
 for state in states:
     print(state)
except MySQLdb.Error as e:
     print("Error executing MySQL query:", e)
finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    # Extract the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states starting with 'N'
    list_states_with_n(username, password, database)
