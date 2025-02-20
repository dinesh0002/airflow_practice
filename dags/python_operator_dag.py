from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner':'dinesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old")


with DAG(
    default_args=default_args,
    dag_id='python_operator_dag',
    description='Running python operator dag',
    start_date=datetime(2025, 2, 20),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_args=['Dinesh', 25]
    )

    task1