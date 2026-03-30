from rq import Queue 
from src.service.redis_conn import redis_conn

queue = Queue("uploads", connection=redis_conn)