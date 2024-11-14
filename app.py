from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)


@app.route('/api/email', methods=['POST'])
def receive_email():
    try:
        data = request.get_json()
        print("Received message:", data)

        producer.send('messages_all', value=data)
        producer.flush()

        response = {
            "status": "success",
            "data": data
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run()