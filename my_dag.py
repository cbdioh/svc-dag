
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# k8s 배포 테스트
def hello():
    print("Hello from Airflow DAG!")

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="sample_hello_dag",
    default_args=default_args,
    description="A simple test DAG",
    schedule="@hourly",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    task_hello = PythonOperator(
        task_id="print_hello",
        python_callable=hello,
    )

