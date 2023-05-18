import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host=" ",
    user= " ",
    password=" "
)

# Create a cursor object to interact with the server
cursor = connection.cursor()

# Execute the query to retrieve the list of databases
cursor.execute("SHOW DATABASES")

# Fetch all the results from the query
databases = cursor.fetchall()

# Print the list of databases
for database in databases:
    print(database[0])

# Close the cursor and connection
cursor.close()
connection.close()
