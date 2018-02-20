#!/usr/bin/env python
import time
import pika

time.sleep(30)

connection = pika.BlockingConnection(pika.URLParameters("amqp://rabbitmq:rabbitmq@localhost:5672"))

channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
