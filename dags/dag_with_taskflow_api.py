from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

default_args = {
    'owner':'dinesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(dag_id='dag_with_taskflow_api_v1',
    default_args=default_args,
    start_date=datetime(2025, 2, 20),
    schedule_interval='@daily')
def dag_with_taskflow_api():
    
    @task(multiple_outputs=True)
    def get_details():
        return {
            'firstname': 'Dinesh',
            'lastname': 'Kumar',
            'age': 25
        }
    
    @task()
    def greet(details):
        print(details)
        print(f"Hello, my name is {details.firstname} {details.lastname} and I am {details.age} years old")
    
    details = get_details()
    greet(details)

dag = dag_with_taskflow_api()