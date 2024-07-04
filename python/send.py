#!/usr/bin/env python
import pika

# establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create queue
channel.queue_declare(queue='hello')

# send message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!'.encode())
print(" [x] Sent 'Hello World!'")

# flush and close connection
connection.close()
