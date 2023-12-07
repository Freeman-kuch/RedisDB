import time
from datetime import datetime
from rq import Queue, Worker, serializers
from rq.command import send_stop_job_command
from task import tasking
from main import r

queue = Queue(
    name="freeman",
    connection=r
)

job = queue.enqueue(
    tasking,
    5,
    job_id="my job id",
    on_success=print("hello World!!!"),
    is_async=False, result_ttl=2000,
    job_timeout=600,
    serializer=serializers.JSONSerializer
)  # default job timeout is usually 180 seconds
timed_job = queue.enqueue_at(datetime(2023,
                                      12,
                                      5,
                                      14,
                                      45, ),
                             tasking,
                             5,
                             result_ttl=1000,
                             serializer=serializers.JSONSerializer)
# print(job.get_id())
print(job.latest_result())
job.fetch(job.get_id())
result = job.latest_result()
if result.type.SUCCESSFUL:
    print(f"Done and was successful {result.return_value}")  # the return value only returns not none value
else:
    send_stop_job_command(r, job_id=job.get_id())
    print(result.exc_string)
# print(timed_job.get_id())
# print(timed_job.is_finished)
# print(len(queue))
# queue.empty()
# queue.delete(delete_jobs=True)
# print(len(queue))
worker = Worker([queue], connection=r, name="test_Worker")
worker.work()
print(Worker.count(connection=r))