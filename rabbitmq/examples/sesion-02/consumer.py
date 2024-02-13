import pika
import json

creds = pika.PlainCredentials('admin','admin')

parameters = pika.ConnectionParameters(
    host            =   '172.17.8.220',
    port            =   5672,
    virtual_host    =   '/',
    credentials     =   creds)

connection = pika.BlockingConnection( parameters)

channel = connection.channel()

# Se prepara un receptor

def callback_receptor(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(
    queue               =   'queue.events',
    auto_ack            =   True,
    on_message_callback =   callback_receptor)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()

