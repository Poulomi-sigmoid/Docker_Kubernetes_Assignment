from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from create_new_db import create_sql_table
from insert_into_emp import insert_into_sql_table

default_args = {
    "owner": "Poulomi",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 20),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG("Dag_docker", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='create_sql_table', python_callable=create_sql_table, dag=dag)
t2 = PythonOperator(task_id='insert_sql_table', python_callable=insert_into_sql_table, dag=dag)

t1 >> t2