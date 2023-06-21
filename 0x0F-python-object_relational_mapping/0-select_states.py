import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database, host='localhost', port=3306)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

# Run the script with the provided arguments
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)

