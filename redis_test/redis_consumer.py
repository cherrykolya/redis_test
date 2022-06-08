import json
from datetime import datetime

from redis import Redis

QUEUE_NAME = "test"

connection = Redis()

while True:
    try:
        data = connection.lpop(QUEUE_NAME)
        if data:
            print(str(datetime.now()) + "CONSUMER :" + str(json.loads(data)))
    except Exception as e:
        print(e)
