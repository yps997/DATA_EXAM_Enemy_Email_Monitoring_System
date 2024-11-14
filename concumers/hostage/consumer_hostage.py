from kafka import KafkaConsumer
import json

class Consumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'message_hostage',
            bootstrap_servers=['localhost:9092'],
            group_id='group_2',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def process_message(self, message):
        try:
            order_data = message.value
        except Exception as e:
            print(f"Error processing the hostage message: {str(e)}")

    def start_listening(self):
        try:
            print("hostage listening...")
            for message in self.consumer:
                self.process_message(message)
        except Exception as e:
            print(f"Error hostage listening: {str(e)}")
        finally:
            self.consumer.close()

if __name__ == "__main__":
    consumer = Consumer()
    consumer.start_listening()