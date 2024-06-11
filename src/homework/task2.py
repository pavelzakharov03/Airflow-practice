import datetime
import pendulum
from datetime import datetime
from airflow.decorators import dag, task

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 11),
    'catchup': False
}


@dag(chedule_interval="0 0 * * *",
     start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
     catchup=False,
     dagrun_timeout=datetime.timedelta(minutes=60),
     default_args=dict(retries=3, retry_delay=datetime.timedelta(minutes=5)), )
def et1():
    @task
    def start():
        ...

    @task
    def stop_task():
        ...

    @task
    def t1():
        ...

    @task
    def t2_1():
        ...

    @task
    def t2_2():
        ...

    @task
    def t2_3():
        ...

    @task
    def t3_1():
        ...

    @task
    def t3_2():
        ...

    @task
    def t3_3():
        ...

    @task
    def t4():
        ...

    @task
    def end():
        ...

    start >> stop_task
    start >> t1
    t1 >> t2_1
    t1 >> t2_2
    t1 >> t2_3
    t2_1 >> t3_1
    t2_2 >> t3_2
    t2_3 >> t3_3
    t3_1 >> t4
    t3_2 >> t4
    t3_3 >> t4
    t4 >> end