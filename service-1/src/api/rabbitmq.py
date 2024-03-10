import pika, sys, os

AMQP_URL = "amqps://trmxqrmt:hbXsbB_LVentl920sEEGFAp45yfmk41u@hawk.rmq.cloudamqp.com/trmxqrmt"

def send(id):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='emails')

    channel.basic_publish(exchange='', routing_key='emails', body=str(id))
    print(f"INFO:     Sent {id} to RabbitMQ")
    connection.close()

# if __name__ == "__main__":
#     send('juukiol98i7kuj')