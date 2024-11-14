from kafka import KafkaConsumer
import json
from tables import ExplosiveMessage, ExplosiveLocation, ExplosiveDevice, ExplosiveSentence
from sqlalchemy.orm import Session
from database.posrtgreSql import engine

session = Session(engine)

class Consumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'messages_explosive',
            bootstrap_servers=['localhost:9092'],
            group_id='group_1',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def process_message(self, message):
        try:
            data = message.value

            explosive_message = ExplosiveMessage(
                id=data['id'],
                email=data['email'],
                username=data['username'],
                ip_address=data['ip_address'],
                created_at=data['created_at']
            )
            session.add(explosive_message)

            if 'location' in data:
                location = ExplosiveLocation(
                    message_id=data['id'],
                    latitude=data['location']['latitude'],
                    longitude=data['location']['longitude'],
                    city=data['location']['city'],
                    country=data['location']['country']
                )
                session.add(location)

            if 'device_info' in data:
                device = ExplosiveDevice(
                    message_id=data['id'],
                    browser=data['device_info']['browser'],
                    os=data['device_info']['os'],
                    device_id=data['device_info']['device_id']
                )
                session.add(device)

            if 'sentences' in data:
                for sentence in data['sentences']:
                    sentence_record = ExplosiveSentence(
                        message_id=data['id'],
                        text=sentence
                    )
                    session.add(sentence_record)

            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error processing the explosive message: {str(e)}")

    def start_listening(self):
        try:
            print("explosive listening")
            for message in self.consumer:
                self.process_message(message)
        except Exception as e:
            print(f"Error explosive listening: {str(e)}")
        finally:
            self.consumer.close()

if __name__ == "__main__":
    consumer = Consumer()
    consumer.start_listening()