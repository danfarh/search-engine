from kafka import KafkaProducer
from config.elasticsearch import create_index
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()


def read_data(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return data


def json_serializer(value):
    return json.dumps(value).encode('utf-8')


def main():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)
    data = read_data('product.json')

    for i in range(len(data)):
        print(data[i])
        producer.send('products', data[i])
        time.sleep(2)


if __name__ == "__main__":
    create_index(os.getenv('INDEX'))
    main()
