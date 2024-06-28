from confluent_kafka import Consumer, KafkaError
from scheduler.transform import Transform
import json, os, threading
from dotenv import load_dotenv

load_dotenv()

# Configurações do Kafka Consumer
conf = {
    'bootstrap.servers': os.environ.get('KAFKA_HOST'),
    'group.id': 'fastapi-consumer',
    'auto.offset.reset': 'earliest'
}
print(f"Scheduler service conectando ao Kafka {str(conf)}")
consumer = Consumer(conf)
transform = Transform()


def consume_messages(topic):
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        # Processa a message
        message = json.loads(msg.value().decode('utf-8'))
        transform.send_to_api(message)
        print(f"Received message: {message}")

def start_consumer():
    topic_kafka = os.environ.get('KAFKA_TOPIC_CADASTRO_PRODUTO')
    thread = threading.Thread(target=consume_messages, args=(topic_kafka,), daemon=True)
    thread.start()
