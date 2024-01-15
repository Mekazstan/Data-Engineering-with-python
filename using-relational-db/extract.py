import mysql.connector
import csv

# MySQL connection parameters
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'R0ot!23#',
    'database': 'dataengineering',
}

# Connect to MySQL
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

# SQL query to select all data from the users table
select_query = "SELECT * FROM users"

# Execute the query
cursor.execute(select_query)

# Fetch all the rows
rows = cursor.fetchall()

# CSV file path
csv_file_path = 'users_data.csv'

# Write data to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    header = [i[0] for i in cursor.description]
    csv_writer.writerow(header)

    # Write data rows
    csv_writer.writerows(rows)

# Close the connection
cursor.close()
connection.close()

print(f"Data exported to {csv_file_path}")
