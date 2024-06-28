from confluent_kafka import Producer
import json, os
from dotenv import load_dotenv

load_dotenv()

# Configurações do Kafka Producer
conf = {
    'bootstrap.servers': os.environ.get('KAFKA_HOST'),
    'client.id': 'fastapi-producer'
}
print(f"API conectando ao Kafka {str(conf)}")
producer = Producer(**conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_message(topic, message):
    message_json = json.dumps(message)
    producer.produce(topic, message_json.encode('utf-8'), callback=delivery_report)
    producer.flush()
