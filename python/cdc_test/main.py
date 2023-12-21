import os
import json

from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError
import asyncio
import socket
import time
from loguru import logger

async def consume():
    topic = os.getenv("KAFKA_CDC_TOPIC", "test-topic")
    bootstrap_servers = os.getenv("KAFKA_CDC_BOOTSTRAP_SERVERS", "localhost:9092")
    group_id = os.getenv("KAFKA_CDC_GROUP_ID", socket.gethostname())

    consumer = None
    max_retries = 5

    for i in range(max_retries):
        try:
            consumer = AIOKafkaConsumer(
                topic, bootstrap_servers=bootstrap_servers, group_id=group_id
            )

            # Get cluster layout and join group `my-group`
            await consumer.start()
            break
        except KafkaConnectionError:
            logger.error("Would not connect... sleeping")
            await consumer.stop()
            time.sleep(1)

    if not consumer:
        logger.error("Could not resolve kafka host")
        return

    try:
        # Consume messages
        async for msg in consumer:
            value = msg.value

            if value:
                value = json.loads(msg.value.decode("utf-8"))

            timestamp = msg.timestamp

            logger.info(f"consumed: {value=} {timestamp=}")

    except Exception as e:
        logger.error(str(e))
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
