from rq import Queue
from redis import Redis

redis_conn = Redis()
q = Queue('low', connection=redis_conn) 

# Getting the number of jobs in the queue
print(len(q))
queued_job_ids = q.job_ids
print(queued_job_ids)
job = q.fetch_job(queued_job_ids[0])
print(job)
