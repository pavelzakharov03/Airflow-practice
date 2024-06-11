import datetime
import pendulum
from datetime import datetime
from airflow.decorators import dag, task


@dag(start_date=datetime(2022,11,1),
    schedule="@daily",
    catchup=False)
def etl():
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

    start() >> [op1(), op2()] >> some_other_task() >> [op3(), op4()] >> end()


dag1 = etl()
