from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import sys
import os
#sys.path.append(os.path.abspath(".."))
from scripts.loading import DataLoader
from scripts.database import Connection

default_args = {
    'owner': 'Mohammed',
    'depends_on_past': False,
    'email': ['mohammedesam.mem@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': datetime(2022, 10, 5),
    'retry_delay': timedelta(minutes=5)
}


def read_and_data():
    """csv data reading and add uuid column
    """
    dl = DataLoader()
    df = dl.read_csv('./data/BTC-USD.csv')
    df.to_csv('./BTC.csv',index=False)

def create_table():
    con = Connection()
    con.create_table()

def insert_data_to_db():
    """Insert data to db"""
    con = Connection()
    price = pd.read_csv('./BTC.csv')
    con.df_to_sql('BTC_price', price)

with DAG(
    dag_id='data_to_postgres_loader',
    default_args=default_args,
    description='Read csv, extract, and put to postgres',
    schedule_interval='@once',
    catchup=False
) as dag:
    data_reader_modifier = PythonOperator(
        task_id='read_data',
        python_callable=read_and_data
    )
    table_creator = PythonOperator(
        task_id='table_creator',
        python_callable=create_table
    )
    insert_data = PythonOperator(
        task_id='insert_data_to_db',
        python_callable=insert_data_to_db
    )

data_reader_modifier>>table_creator>>insert_data