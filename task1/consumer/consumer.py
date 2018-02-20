#!/usr/bin/env python
import time
import pika
import pymongo
from pymongo import MongoClient

time.sleep(10)

flag = 0

connection = pika.BlockingConnection(pika.URLParameters("amqp://rabbitmq:rabbitmq@rabbit"))

channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %s" % (body,))
    client = MongoClient('mongodb://alice:abc123@localhost:27017')
    db = client.sampleDB
    if not flag:
        db.create_collection("strings")
    collection = db['strings']

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
