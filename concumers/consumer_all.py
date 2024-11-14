from kafka import KafkaConsumer, KafkaProducer
import json


class Consumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'messages_all',
            bootstrap_servers=['localhost:9092'],
            group_id='order_processing_group',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

