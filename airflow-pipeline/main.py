# Dag Scheduling libraries
import datetime as dt
from datetime import timedelta

# Data Transformation/Manipulation library
import pandas as pd

# Task Building libraries
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


# Function to read a CSV file and writes it out to JSON
def CSVToJson():
    # Reading the csv
    df=pd.read_CSV('/home/chukwuemeka/Documents/DataWithPY/data.CSV')
    for i,r in df.iterrows():
        print(r['name'])
        df.to_JSON('fromAirflow.JSON',orient='records')
        
# DAG Arguments        
default_args = {
    'owner': 'mekazstan',
    'start_date': dt.datetime(2023, 1, 10),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG', # Dag ID
    default_args=default_args,
    schedule_interval=timedelta(minutes=5), # How often to run the dag
    # '0 * * * *',
) as dag:
    print_starting = BashOperator(task_id='starting', bash_command='echo "I am reading the CSV now....."')
    CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVToJson)
    
# print_starting.set_downstream(CSVJson)
# CSVJson.set_upstream(print_starting)

print_starting >> CSVJson
CSVJson << print_starting
    
    
    
    
    
    
    
    
    
    
    
    
# a) @once
# b) @hourly – 0 * * * *
# c) @daily – 0 0 * * *
# d) @weekly – 0 0 * * 0
# e) @monthly – 0 0 1 * *
# f) @yearly – 0 0 1 1 *
# format [minute, hour, day of month, month, day of week]