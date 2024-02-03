import pika, json
import random, time

creds = pika.PlainCredentials(username = 'admin', password = 'admin')

parameters = pika.ConnectionParameters(
    host            =   '172.17.8.220',
    port            =   5672,
    virtual_host    =   '/',
    credentials     =   creds)

connection = pika.BlockingConnection( parameters)

channel = connection.channel()

channel.queue_declare(queue = 'queue.events') #, durable=True)

properties = pika.BasicProperties(
    # make message persistent
    delivery_mode = 2)

message = {
    'eventType': 'PagoRealizado',
    'payload': {
        'operacion': {
            'numero': 1234567890,
            'fecha': '2024-01-31T00:00:00',
            'monto': 1000.00,
            'comercio': 1,
            'terminal': 1
        }
    }
}

#while True:
#  sleep_time = random.uniform(1, 5)
#  time.sleep(sleep_time)
channel.basic_publish(exchange='', 
    routing_key =   'queue.events',
    body        =   json.dumps(message),
    properties  =   properties)

print(" [x] Message Sent to 'queue.events'")
