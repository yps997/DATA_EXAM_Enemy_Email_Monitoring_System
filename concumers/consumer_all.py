from kafka import KafkaConsumer, KafkaProducer
import json


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

    def filtered_hostage_word(self, message_data):
        keywords = ['hostage']
        message_text = str(message_data).lower()
        return any(keyword in message_text for keyword in keywords)

    def filtered_explosive_word(self, message_data):
        keywords = ['explosive']
        message_text = str(message_data).lower()
        return any(keyword in message_text for keyword in keywords)

    def process_message(self, message):
        ###להוסיף שליחת הודעה למונגו
        try:
            message_data = message.value
            if self.filtered_hostage_word(message_data):
                self.producer.send('hostages_alerts', value=message_data)
                print(f"hostage message sending: {message_data}")

            if self.filtered_explosive_word(message_data):
                self.producer.send('messages_explosive', value=message_data)
                print(f"explosive message sending: {message_data}")

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