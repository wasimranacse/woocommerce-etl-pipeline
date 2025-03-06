# Airflow DAG for automation

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.main import extract_data, transform_data, load_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'schedule_interval': '@daily'
}

dag = DAG('woocommerce_sales_etl', default_args=default_args)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag
)

extract_task >> transform_task >> load_task


