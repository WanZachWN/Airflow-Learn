from datetime import datetime, timedelta

from airflow import DAG

default_args = {
    'owner': 'znawawi',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(

) as dag:
    
