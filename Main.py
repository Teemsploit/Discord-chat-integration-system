from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = ''

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    if message:
        payload = {'content': message}
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:  
            return jsonify({'status': 'Message sent!'}), 200
        else:
            return jsonify({'status': 'Failed to send message!'}), response.status_code
    return jsonify({'status': 'No message provided!'}), 400

if __name__ == '__main__':
    app.run(port=5000)
