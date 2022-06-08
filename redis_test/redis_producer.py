import json
import random
import time
from datetime import datetime

from redis import Redis

QUEUE_NAME = "test"

connection = Redis()

while True:
    message = {"user_id": random.randint(10000, 99999), "text": random.gauss(0, 5.55)}
    connection.lpush(QUEUE_NAME, json.dumps(message))
    print(str(datetime.now()) + " PRODUCER :" + json.dumps(message))
    delay = random.randint(5, 10)
    time.sleep(delay)
