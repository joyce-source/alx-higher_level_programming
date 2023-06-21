import MySQLdb
import sys

def list_states(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database, host='localhost', port=3306)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_states(username, password, database, state_name)
