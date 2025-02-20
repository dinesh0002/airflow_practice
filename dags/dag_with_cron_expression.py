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
    dag_id='cron_dag_v1',
    default_args=default_args,
    description='Running dag with cron expression',
    schedule_interval='0 0 * * *',
    start_date=days_ago(5),
    tags=['cron schedule example']
) as dag:
    task1= BashOperator(
        task_id='task1',
        bash_command='echo "task1"'
    )
    task1