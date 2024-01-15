from faker import Faker
import mysql.connector

# Create a Faker instance
fake = Faker()

# MySQL connection parameters
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '*********',
    'database': 'dataengineering',
}

# Connect to MySQL
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

# Create the users table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    zip VARCHAR(20)
);
"""
cursor.execute(create_table_query)

# Generate and insert random data
for _ in range(1000):
    # Generate random data
    name = fake.name()
    street = fake.street_address()
    city = fake.city()
    zip_code = fake.zipcode()

    # Insert data into the users table
    insert_query = "INSERT INTO users (name, street, city, zip) VALUES (%s, %s, %s, %s)"
    data = (name, street, city, zip_code)
    cursor.execute(insert_query, data)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully.")
