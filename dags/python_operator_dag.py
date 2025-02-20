from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner':'dinesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(age, ti):
    name = ti.xcom_pull(task_ids='xcom_pusher')
    print(name)
    print(f"Hello, my name is {name[0]} and I am {age} years old")


def xcom_pusher(*args):
    return args

with DAG(
    default_args=default_args,
    dag_id='python_operator_dag_v2',
    description='Running python operator dag',
    start_date=datetime(2025, 2, 20),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_args=[25])
    
    task2 = PythonOperator(
        task_id='xcom_pusher',
        python_callable=xcom_pusher,
        op_args=['Testing xcom pusher', 'random', 'args']
    )

    task2 >> task1