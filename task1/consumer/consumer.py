#!/usr/bin/env python
import time
import pika
from pymongo import MongoClient

time.sleep(10)

connection = pika.BlockingConnection(pika.URLParameters("amqp://rabbitmq:rabbitmq@rabbit"))

channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):

    client = MongoClient('mongo')

    db = client['test-database']
    collection = db['test-collection']
    doc = {"author": str(body)}
    collection.insert_one(doc)
    client.close()


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
