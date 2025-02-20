from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'dinesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v6',
    default_args = default_args,
    description='Running first dag to test airflow in docker',
    start_date = datetime(2025, 2, 19, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo 'Hello world this is the first task to start with airflow and docker !'"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo 'Added second task to test and run'"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo task3 will be running after task1 and task2"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    task1 >> task2
    task1 >> task3

    