from kafka import KafkaConsumer, KafkaProducer
import json

from database.mongo import *


class ProducerConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'messages_all',
            bootstrap_servers=['localhost:9092'],
            group_id='order_processing_group',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )


    def process_message(self, message):
        try:
            message_data = message.value
            collection.insert_one(message_data)
            for i, sentence in enumerate(message_data['sentences']):
                if 'explosive' in sentence:
                    found_sentence = message_data['sentences'].pop(i)
                    message_data['sentences'].insert(0, found_sentence)
                    self.producer.send('messages_explosive', value=message_data)
                    print(f"explosive message sending: {message_data}")
                    break
                elif 'hostage' in sentence:
                    found_sentence = message_data['sentences'].pop(i)
                    message_data['sentences'].insert(0, found_sentence)
                    self.producer.send('message_hostage', value=message_data)
                    print(f"hostage message sending: {message_data}")
                    break
            self.producer.flush()

        except Exception as e:
            print(f"Error processing the message: {str(e)}")


    def start_listening(self):
        try:
            print("start listening to messages_all... ")
            for message in self.consumer:
                self.process_message(message)
        except Exception as e:
            print(f"error listening: {str(e)}")
        finally:
            self.consumer.close()
            self.producer.close()


if __name__ == "__main__":
    consumer = ProducerConsumer()
    consumer.start_listening()
