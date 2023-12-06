import time, os
from rq import get_current_job
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def tasking(x: int):
    job = get_current_job()
    print("staring queue")
    for i in range(x):
        job.meta["progress"] = 100.0 * i / x
        job.save_meta()
        print(x)
        print(job.meta)
        time.sleep(x)
        x = x - 1
    job.meta["progress"] = 100
    job.save_meta()
    print("DONE")