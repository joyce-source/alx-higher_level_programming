#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb

def list_states(username, password, database):

    """
Connects to the MySQL server and lists all states from the specified database
Arguments:
        - username: MySQL username
        - password: MySQL password
        - database: Database name
"""

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, username='root', passwd='root', db='database')

# Create a cursor object to interact with the database
cursor = db.cursor()

try:
# Execute the query to retrieve all states
 query = "SELECT * FROM states ORDER BY id ASC"
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
# Provide your MySQL username, password, and database name
 username = 'root'
 password = 'root'
 database = "hbtn_0e_0_usa"

# Call the function to list states
 list_states(username, password, database)

