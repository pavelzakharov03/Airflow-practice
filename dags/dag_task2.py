import datetime
import pendulum
from datetime import datetime
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 11),
    'catchup': False
}


@dag(start_date=datetime(2022,11,1),
    schedule="@daily",
    catchup=False)
def etl2():
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

    start() >> stop_task()
    chain(start(), t1(), [t2_1(), t2_2(), t2_3()], [t3_1(), t3_2(), t3_3()], t4(), end())


dag2 = etl2()