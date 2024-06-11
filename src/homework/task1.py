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
    def op1():
        ...

    @task
    def op2():
        ...

    @task
    def some_other_task():
        ...

    @task
    def op3():
        ...

    @task
    def op4():
        ...

    @task
    def end():
        ...

    start >> op1
    start >> op2
    op1 >> some_other_task
    op2 >> some_other_task
    some_other_task >> op3
    some_other_task >> op4
    op3 >> end
