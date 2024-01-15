"""_summary_
    This dag combines two Python operators to achieve these tasks:
    - Extract data from MYSQL DB & save it as a CSV file.
    - Read it in and write it to a Mongodb collection as individual documents. 
"""

# Dag Scheduling libraries
import datetime as dt
from datetime import timedelta

# Data Transformation/Manipulation library
import pandas as pd
import csv

# Task Building libraries
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# 1st method Dag creation

# Function to extract data from MYSQL DB & save to a CSV file.
def extract_from_mysql():
    import mysql.connector

    # MySQL connection parameters
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '********',
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
    

# Function to write data to a Mongodb collection as individual documents.
def write_to_mongodb_collection():
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db_name = 'dewithpython'
    db = client[db_name]

    # Check if the database exists, create it if not
    if db_name not in client.list_database_names():
        print(f"Creating MongoDB database: {db_name}")
        db = client[db_name]

    collection = db['users']

    # Specify the CSV file path
    csv_file_path = 'user_data.csv'
    # Read data from CSV and insert into MongoDB collection
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            user_data = {
                'name': row['name'],
                'street': row['street'],
                'city': row['city'],
                'zip': row['zip'],
            }

            # Insert data into MongoDB collection
            collection.insert_one(user_data)

    print("Data inserted into MongoDB.")

        
# DAG Arguments        
default_args = {
    'owner': 'mekazstan',
    'start_date': dt.datetime(2024, 1, 15),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyDBDAG', # Dag ID
    default_args=default_args,
    schedule_interval=timedelta(minutes=480)
) as dag:
    extract_from_mysql = PythonOperator(task_id='mysql_extractor', python_callable=extract_from_mysql)
    write_to_mongodb_collection = PythonOperator(task_id='mongodb_writer', python_callable=write_to_mongodb_collection)

# Order Sequence
extract_from_mysql >> write_to_mongodb_collection
