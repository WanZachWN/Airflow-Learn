from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'znawawi',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='firstname')
    last_name = ti.xcom_pull(task_ids='get_name', key='lastname')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}," 
          f" and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key='firstname', value='Jerry')
    ti.xcom_push(key='lastname', value='Fridman')

def get_age(ti):
    ti.xcom_push(key='age', value=19)


with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_v04',
    description='Our first DAG using python operator',
    start_date=datetime(2023, 6, 7),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        # op_kwargs={'age': '20'}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    
    [task2, task3] >> task1
