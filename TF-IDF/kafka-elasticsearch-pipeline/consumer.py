from kafka import KafkaConsumer
import json
import os
from config.elasticsearch import insert_data
from dotenv import load_dotenv
load_dotenv()


def main():
    consumer = KafkaConsumer('products', bootstrap_servers=[
                             'localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    for i, data in enumerate(consumer):
        insert_data(os.getenv('INDEX'), i, data.value)


if __name__ == "__main__":
    main()
