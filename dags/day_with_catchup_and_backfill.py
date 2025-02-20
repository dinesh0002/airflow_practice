from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner':'dinesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}   

with DAG(
    dag_id='dag_with_catchup_and_backfill',
    default_args=default_args,
    description='dag example with backfill and catchup',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(5),
    tags=['example'],
    catchup=True
) as dag:
    task1= BashOperator(
        task_id='task1',
        bash_command='echo "task1"'
    )