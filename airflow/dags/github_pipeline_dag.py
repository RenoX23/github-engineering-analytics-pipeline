from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "renold",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    dag_id="github_analytics_pipeline",
    default_args=default_args,
    description="GitHub Engineering Analytics Pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    run_pipeline = BashOperator(
        task_id="run_github_pipeline",

        bash_command=(
            "cd /opt/airflow/project && "
            "python -m app.main"
        )
    )

    run_pipeline
