from rq import Queue
from redis import Redis
import time
from count import count_words_at_url




def send_msg_2_q():
	# Tell RQ what Redis connection to use
	redis_conn = Redis(host='localhost', port=6379, db=0)
	q = Queue('low', connection=redis_conn)  
	# no args implies the default queue

	# Delay execution of count_words_at_url('http://nvie.com')
	job = q.enqueue(count_words_at_url, "http://nvie.com")
	print(job.result)   # => None

	# Now, wait a while, until the worker is finished
	time.sleep(2)
	print(job.result)   # => 889



if __name__ == "__main__":
	while True:
		send_msg_2_q()
		time.sleep(10)
