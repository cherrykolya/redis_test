import asyncio

from redis_test.aioredis_consumer import consumer_process
from redis_test.aioredis_producer import producer_process


async def main():
    await asyncio.gather(producer_process(), consumer_process())


if __name__ == "__main__":
    asyncio.run(main())
