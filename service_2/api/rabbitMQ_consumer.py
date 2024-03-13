from msilib import type_string
import pika
import sys
import json

AMQP_URL = "amqps://trmxqrmt:hbXsbB_LVentl920sEEGFAp45yfmk41u@hawk.rmq.cloudamqp.com/trmxqrmt"
connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
channel = connection.channel()

channel.queue_declare(queue='emails')



global address 



def callback(ch, method, properties, body):
    global address 
    print(f"INFO:     Received {body} from RabbitMQ")
    address = body

    # Stop consuming messages after receiving one item
    channel.basic_cancel(consumer_tag=method.consumer_tag)

def receiveFromRabbitMQ():
    print(2)
    channel.basic_consume('emails', callback, auto_ack=True)
    print(3)
    print('INFO:     Waiting for messages...')
    channel.start_consuming()



def get_address():
# Assuming the value is stored in a variable called 'byte_string'
   

    # Convert the byte string to a regular string
    regular_string = address.decode('utf-8')

    print(regular_string)

    return regular_string

if __name__ == "__main__":
    receiveFromRabbitMQ()