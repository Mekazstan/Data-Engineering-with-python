from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def filter_records():
    # Read the CSV file
    df = pd.read_csv('/home/chukwuemeka/Documents/DataWithPY/data.csv')

    # Filter records for people over the age of 40
    filtered_df = df[df['age'] > 40]

    # Write filtered records to a new CSV file
    filtered_df.to_csv('/home/chukwuemeka/Documents/DataWithPY/filtered_data.csv', index=False)

# DAG configuration
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2024, 1, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_processing_pipeline',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define the PythonOperator to execute the filter_records function
filter_records_task = PythonOperator(
    task_id='filter_records_task',
    python_callable=filter_records,
    dag=dag,
)

# Set the task dependencies
filter_records_task

if __name__ == "__main__":
    dag.cli()
