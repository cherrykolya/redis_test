import json
from datetime import datetime

from aioredis import Redis

QUEUE_NAME = "test"

connection = Redis()


async def consumer_process():
    while True:
        try:
            data = await connection.rpop(QUEUE_NAME)
            if data:
                print(str(datetime.now()) + " CONSUMER: " + str(json.loads(data)))
        except Exception as e:
            print(e)
