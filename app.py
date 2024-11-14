from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.get_json()
    print("Received message:", data)
    response = {
        "status": "success",
        "data": data
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
