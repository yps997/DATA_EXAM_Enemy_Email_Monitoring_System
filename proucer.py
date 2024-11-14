from kafka import KafkaProducer
import json

class Producer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, message_data):
        try:
            self.producer.send('messages_all', message_data)
            self.producer.flush()
            print(f"message send: {message_data}")
        except Exception as e:
            print(f"error message not send: {str(e)}")

