"""_summary_
    Data cleaning & filtering using airflow
    STEPS
    - Clean the users data [Here a new column will be addedto the dataset to group the data by countries]
    - Filter the new cleaned data by country 
    - Save the new selected data in the csv to desktop 
"""

# Dag Scheduling libraries
import datetime as dt
from datetime import timedelta

# Data storage library
import csv
import pandas as pd 

# Task Building libraries
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BashOperator


# Define a function to map city to country based on the starting letter
def map_city_to_country(city):
    if 'A' <= city[0].upper() <= 'H':
        return 'Country A'
    elif 'I' <= city[0].upper() <= 'R':
        return 'Country B'
    elif 'S' <= city[0].upper() <= 'Z':
        return 'Country C'
    else:
        return 'Unknown Country'

# Data cleaning function
def cleanUsers():
    df = pd.read_csv('/home/chukwuemeka/Documents/DataWithPY/airflow-pipeline/users_data.csv')
    # Create a new 'country' column by applying the mapping function to the 'city' column
    df['country'] = df['city'].apply(map_city_to_country)

    # Save the DataFrame to a new CSV file
    df.to_csv('/home/chukwuemeka/Documents/DataWithPY/airflow-pipeline/clean_users.csv', index=False)

    # Display the updated DataFrame
    print(df[['city', 'country']])

    
# Data filtering function
def filterData():
    df=pd.read_csv('/home/chukwuemeka/Documents/DataWithPY/airflow-pipeline/clean_users.csv')
    # Filter the DataFrame based on the 'country' column
    filtered_df = df[df['country'] == 'Country A']
    filtered_df.to_csv('/home/chukwuemeka/Documents/DataWithPY/airflow-pipeline/country_a_users.csv')

# DAG Arguments        
default_args = {
    'owner': 'mekazstan',
    'start_date': dt.datetime(2024, 1, 17),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyDBDAG', # Dag ID
    default_args=default_args,
    schedule_interval=timedelta(minutes=480)
) as dag:
    cleanData = PythonOperator(task_id='clean', python_callable=cleanUsers)
    selectData = PythonOperator(task_id='filter', python_callable=filterData)
    copyFile = BashOperator(task_id='copy',bash_command='cp /home/chukwuemeka/Documents/DataWithPY/airflow-pipeline/country_a_users.csv /home/chukwuemeka/Desktop')

# Order Sequence
cleanData >> selectData >> copyFile
