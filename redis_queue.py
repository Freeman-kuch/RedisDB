import time
from datetime import datetime
from rq import Queue, Worker
from task import tasking
from main import r

queue = Queue(
    name="freeman",
    connection=r
)

job = queue.enqueue(tasking, 5, job_id="my job id", on_success=print("hello World!!!"), is_async=False, result_ttl=2000, job_timeout=600)
timed_job = queue.enqueue_at(datetime(2023, 12, 5, 14, 45, ), tasking, 5)
# print(job.get_id())
# print(job.is_finished)
# print(timed_job.get_id())
# print(timed_job.is_finished)
# print(len(queue))
# queue.empty()
# queue.delete(delete_jobs=True)
# print(len(queue))
worker = Worker([queue], connection=r, name="test_Worker")
worker.work()
print(Worker.count(connection=r))